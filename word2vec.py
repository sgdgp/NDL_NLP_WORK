# -*- coding: utf-8 -*-

import gensim

class MySentences(object):
    def __init__(self, fname):
        self.fname = fname
 
    def get_sentence_list(self):
        sent = []
        with open(self.fname,'r') as fin:
            for line in fin:
                line = (line.strip()).split()
                sent.append(line)
        return sent       
            
def word2vec_main():
    sentences = MySentences('cayasongi.txt').get_sentence_list()
    model = gensim.models.word2vec.Word2Vec(sentences=sentences,min_count=1)
    print model.similarity('প্রতি','প্রতি')
    
def word2vec_test():
    # testing 
    s = "He is a man"
    s = s.strip()
    s = s.split()
    s2 = []
    s2.append(s)
    print s
    model = gensim.models.word2vec.Word2Vec(sentences=s2,min_count=1)
    # model = gensim.models.Word2Vec(sentences=s,min_count=1)
    print model.vocab
    print model.similarity('man','man')
    
def main():
    # word2vec_test()
    word2vec_main()        
if __name__=="__main__":
    main()               