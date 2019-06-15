# class Builder
# 1: preprocess train doc
# 2: create tree
# 3: create n sample
import sys
sys.path.extend(['/home/ddragon/PycharmProjects/Ngram-LM'])
from src.model.NgramModel import NgramLanguageModel

# Each sentences must be on one line
# CORPUS  = '../../data/HarryPotter/Harry Potter 1 - Hon Da Phu Thuy.txt'
# with open(CORPUS, 'r') as handle:
#     doc = handle.read()
# handle.close()
# sents = doc2sentences(doc)

# with open("sentperline_"+CORPUS.split('/')[-1], 'w') as handle:
#     for sent in sents:
#         handle.write(sent+'\n')
# handle.close()



CORPUS = 'sentperline_Harry Potter 1 - Hon Da Phu Thuy.txt'
lm = NgramLanguageModel(N=3)
lm.fit(CORPUS)
samples = lm.generate_samples(20)
with open('n_samples.txt', 'w') as wr:
    for s in samples:
        wr.write(s+'\n')
wr.close()
lm.write_freqs_down()
