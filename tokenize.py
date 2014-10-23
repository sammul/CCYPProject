#-*- coding: UTF-8 -*-
'''
Created on Oct 23, 2014

@author: Wu Xia
'''
import sys
import re

def main():
    reload(sys)  
    sys.setdefaultencoding('utf8') 
    
    fn = sys.argv[1] #dict_name
    f = open(fn,'r')
    dic = set()
    for line in f:
        line = replace(line)
        dic.add(line)
        
    f.close()
    
    while True:
        line = raw_input()
        line = line.encode('utf-8')
        words = line.split()
        for word in words:
            tokenize(word,dic)

    
def tokenize(sentence, dic):
    sentence =sentence.decode('utf-8')
    l = len(sentence)
    while l>0 :
        s = 0
        while s<l:
            if sentence[s:l] in dict:
                print sentence[s:l]
                break
            s+=1
        if s==l:
            print sentence[s-1:l]
        else:
            l=s

def replace(word):
    return re.sub('[" \n]', '', word)    

if __name__ == '__main__':
    main()