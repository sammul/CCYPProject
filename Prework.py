#encoding=utf-8
'''
Created on Oct 17, 2014

@author: Wu Xia
'''
import re
import sys

def main():
    reload(sys)  
    sys.setdefaultencoding('utf8') 
    
    origin = open(sys.argv[1],'r')
    #origin.readline(); #first line is not data
    dict = {}
    out = open(sys.argv[2],'w')
    tune = ['','ˊ','ˇ','ˋ','·']
    for line in origin:
        line = line.encode('utf-8')
        words = line.split(',') #1 zhuyin 2 pinyin 4 character
        zhuyin = replace(words[1])
        zhuyin += tune[int(words[3])-1]
        pinyin = replace(words[2])
        characters = replace(unicode(replace(words[4]),'utf-8'))
        for c in characters:
            if dict.has_key(c):
                if zhuyin not in dict[c]['zhu']:
                    dict[c]['zhu'].add(zhuyin)
                if pinyin not in dict[c]['pin']:
                    dict[c]['pin'].add(pinyin)
            else:
                dict[c] = {}
                dict[c]['zhu'] = set([zhuyin])
                dict[c]['pin'] = set([pinyin])
        
    for k in dict.keys():
        output = k+";"
        output += ",".join(dict[k]['zhu'])+";"
        output += ",".join(dict[k]['pin'])+"\n"
        out.write(output.encode('utf-8'))
    
    out.close()
    origin.close()

def replace(word):
    return re.sub('[" \n]', '', word)

if __name__ == '__main__':
    main()