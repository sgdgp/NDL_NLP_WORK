# -*- coding: utf-8 -*-

import gensim

class MySentences(object):
    def __init__(self, fname):
        self.fname = fname
 
    def __iter__(self):
        for line in open(self.fname,'r'):
            print line
            yield line.split()
            
            
def main():
    # sentences = MySentences('cayasongi.txt')
    # print sentences 
    s = "প্রতি বছর শীতের ছুটির সময় ভাবি কিছুদিন গ্রামে কাটিয়ে আসব। দলবল নিয়ে যাব- হৈচৈ করা যাবে। আমার বাচ্চারা কখনও গ্রাম দেখেনি- তারা খুশি হবে। পুকুরে ঝাঁপাঝাঁপি করতে পারবে। শাপলা ফুল শুধু যে মতিঝিলের সামনেই ফোটে না, অন্যান্য জায়গাতেও ফোটে তাও স্বচক্ষে দেখবে।"
    sent = []
    s = (s.strip()).split(' ')
    sent.append(s)
    print sent
    
    s2 = "আমার বেশির ভাগ পরিকল্পনাই শেষ পর্যন্ত কাজে লাগাতে পারি না। এটা কেমন করে জানি লেগে গেল। একদিন সত্যি সত্যি রওনা হলাম।"
    sent2 = []
    s2 = s2.strip()
    s2 = s2.split(' ')
    sent2.append(s2)
    
    model = gensim.models.Word2Vec(sentences=s,min_count=1)
    # model.build_vocab
    model.train(sent2)
    model.save('Word2VecModel.txt') 
    print "done"
    print model.similarity('আমার','বেশির')
    
if __name__=="__main__":
    main()               