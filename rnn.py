# -*- coding: utf-8 -*-

import nltk
import itertools
import numpy as np

def tokenize():
        
    vocabulary_size = 100000
    unknown_token = "UNKNOWN_TOKEN"
    sentence_start_token = "SENTENCE_START"
    sentence_end_token = "SENTENCE_END"
    
    # Read the data and append SENTENCE_START and SENTENCE_END tokens
    print "Reading data file..."
    with open('cayasongi.txt', 'rb') as f:
        # reader = csv.reader(f, skipinitialspace=True)
        # reader.next()
        # Split full comments into sentences
        # sentences = itertools.chain(*[nltk.sent_tokenize(x[0].decode('utf-8').lower()) for x in f])
        sentences = itertools.chain(*[nltk.sent_tokenize(x[0]) for x in f])
        
        # Append SENTENCE_START and SENTENCE_END
        sentences = ["%s %s %s" % (sentence_start_token, x, sentence_end_token) for x in sentences]
    print "Parsed %d sentences." % (len(sentences))
        
    # Tokenize the sentences into words
    tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]
    
    # Count the word frequencies
    word_freq = nltk.FreqDist(itertools.chain(*tokenized_sentences))
    print "Found %d unique words tokens." % len(word_freq.items())
    
    # Get the most common words and build index_to_word and word_to_index vectors
    vocab = word_freq.most_common(vocabulary_size-1)
    index_to_word = [x[0] for x in vocab]
    index_to_word.append(unknown_token)
    word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])
    
    print "Using vocabulary size %d." % vocabulary_size
    print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[-1][0], vocab[-1][1])
    
    # Replace all words not in our vocabulary with the unknown token
    for i, sent in enumerate(tokenized_sentences):
        tokenized_sentences[i] = [w if w in word_to_index else unknown_token for w in sent]
    
    print "\nExample sentence: '%s'" % sentences[0]
    print "\nExample sentence after Pre-processing: '%s'" % tokenized_sentences[0]
    
    # Create the training data
    X_train = np.asarray([[word_to_index[w] for w in sent[:-1]] for sent in tokenized_sentences])
    y_train = np.asarray([[word_to_index[w] for w in sent[1:]] for sent in tokenized_sentences])


    # print tokenized_sentences


def bangla_sentence_tokenize():
    unknown_token = "UNKNOWN_TOKEN"
    sentence_start_token = "SENTENCE_START"
    sentence_end_token = "SENTENCE_END"
    te = nltk.word_tokenize('অনেকদিন পর গ্রামে গিয়ে ভালো লাগল। দেখলাম আমার বাচ্চাদের আনন্দবর্ধনের সব ব্যবস্থাই নেওয়া হয়েছে।')
    sent = []
    
    s = sentence_start_token + ' '
    for t in te:
        if t!=t.rstrip('।') :
            s = s+t.rstrip('।')+' '+sentence_end_token
            sent.append(s)
            s = sentence_start_token + ' '
        else :
            s = s + t + ' '
   
    for s in sent:
        print s    
        
        
        
def tokenize_test():
    # text = nltk.word_tokenize("হুমায়ূন আহমেদ")
    # print text
    
    # te = nltk.word_tokenize('অনেকদিন পর গ্রামে গিয়ে ভালো লাগল। দেখলাম আমার বাচ্চাদের আনন্দবর্ধনের সব ব্যবস্থাই নেওয়া হয়েছে।')
    # for t in te:
    #     print t.rstrip('।')
        
    # print ['।'] 
    bangla_sentence_tokenize()   

def main():
    tokenize_test()
    # tokenize()
    
if __name__=="__main__":
    main()