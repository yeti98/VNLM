import codecs


class BasicTokenizer():
    @staticmethod
    def load_puncts():
        with codecs.open('../../data/punct.txt', "r", "utf-8") as handle:
            puncts = set(handle.read().split(' '))
        handle.close()
        return puncts

    PUCNTS = load_puncts.__func__()

    def __init__(self, delimiter=' '):
        self.delimiter = delimiter
        BasicTokenizer.PUCNTS = self.load_puncts()

    def process(self, sens_seqs):
        tokenized_seqs = []
        for w_seq in sens_seqs:
            tokenized_seqs.append(self._tokenize(w_seq))
        return tokenized_seqs

    def _preprocess_punctuation(self, seq):
        new_seq = seq
        for p in self.PUCNTS:
            new_seq = new_seq.replace(p, self.delimiter + p)
        return new_seq.strip()

    def _tokenize(self, seq):
        preprocessed_sequence = self._preprocess_punctuation(seq)
        return preprocessed_sequence.split(self.delimiter)
