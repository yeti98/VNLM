import copy
import pickle
from collections import defaultdict
import astropy.units as u
import astropy.table
from src.model.BasicTokenizer import BasicTokenizer
from src.model.TreeBuilder import TreeBuilder
from src.run.utils import doc2sentences


class Ngram:
    STOP_SIGNAL = 'STOP.'

    def __init__(self, N):
        self.N = N
        self.initial_sequence = ["w#{}".format(-i) for i in range(N - 1, 0, -1)]

    def create_ngram(self, sequence):
        ngrams = []
        new_sequence = self.initial_sequence + sequence + [self.STOP_SIGNAL]
        for index in range(len(new_sequence) - self.N + 1):
            ngrams.append(new_sequence[index:index + self.N])
        return ngrams


class FrequencyModel:
    def __init__(self):
        self.past_seqs = defaultdict(int)
        self.freqs = defaultdict(lambda: defaultdict(int))
        self.number_of_unique_ngrams = 0

    def add_ngram(self, ngram):
        head, tail = self._partition_ngrams(ngram)
        self.past_seqs[head] += 1
        # print(head,'\t' ,tail)
        if self.freqs[head][tail] == 0:
            self.number_of_unique_ngrams += 1
        self.freqs[head][tail] += 1

    def get_ngram_freq(self, ngram):
        head, tail = self._partition_ngrams(ngram)
        return self.past_seqs[head], self.freqs[head][tail]

    def get_ngram_probabilities(self, head, tail):
        head_count, tail_count = self.get_ngram_freq(tuple(list(head) + [tail]))
        return tail_count / head_count

    def _partition_ngrams(self, ngram):
        *head, tail = ngram
        return tuple(head), tail

    def get_all_past_seqs(self):
        return self.past_seqs.keys()

    def get_all_next_words(self, past_seq):
        return self.freqs[past_seq].keys()

    def write(self):
        handle = open("prob.txt", 'w')
        for _ in self.past_seqs.keys():
            handle.write(str(_))
            handle.write('\n')
            for k, v in self.freqs[_].items():
                handle.write('\t' + str(k) + ' :\t' + str(v) + '\n')
            handle.write('**************\n')
        handle.close()
        pass


class NgramLanguageModelSupport:
    '''
    Support stream corpus and generate samples sentences
    '''

    def __init__(self, corpus_path, N):
        self.source = corpus_path
        self.tokenizer = BasicTokenizer()
        self.ngram = Ngram(N)
        self.N = N
        self.sent_count = 0

    def __iter__(self):
        for line in open(self.source, 'r'):
            if len(line.split('n')) > self.N:
                sentence = [line]
                tokenized_sentence = self.tokenizer.process(sentence)
                ngrams = []
                for tks in tokenized_sentence:
                    ngrams.extend(self.ngram.create_ngram(tks))
                # print(ngrams)
                self.sent_count += 1
                yield ngrams
            else:
                yield None

    def get_ngram_model(self):
        return self.ngram

    def get_numberofsents(self):
        return self.sent_count


class NgramLanguageModel:
    def __init__(self, N):
        self.N = N
        self.freq_model = FrequencyModel()
        self.model = None
        self.ngram = None

    def fit(self, path):
        stream_corpus = NgramLanguageModelSupport(path, self.N)
        for gram_list in stream_corpus:
            if gram_list != None:
                for gram in gram_list:
                    self.freq_model.add_ngram(gram)
        print("NUMBER OF SENTENCES:\t", stream_corpus.get_numberofsents())
        self.model = {key: self._create_tree(key) for key in self.freq_model.get_all_past_seqs()}
        self.ngram = stream_corpus.get_ngram_model()
        pass

    def generate_samples(self, number=10):
        sents = []
        for _ in range(number):
            sample_pattern = copy.deepcopy(self.ngram.initial_sequence)
            # print("*",sample_pattern)
            while sample_pattern[-1] != self.ngram.STOP_SIGNAL:
                past_seqs = tuple(sample_pattern[-(self.N - 1):])
                # print(past_seqs)
                next_word = self.model[past_seqs].random_label()
                sample_pattern.append(next_word)
            sent = sample_pattern[len(self.ngram.initial_sequence):-1]

            sents.append(' '.join(sent))
        return sents

    def _create_tree(self, key):
        appearable_words = self.freq_model.get_all_next_words(key)
        probs_list = [self.freq_model.get_ngram_probabilities(key, val) for val in appearable_words]
        tree_object = TreeBuilder(probs_list, appearable_words)
        return tree_object

    def write_freqs_down(self):
        self.freq_model.write()
