#encoding=utf-8
'''
Created on Oct 18, 2014

@author: Wu Xia
'''
import re
from xml.dom import minidom


def main():
    dic = {}
    dicfile = open('dictionary.txt','r')
    for line in dicfile:
        line = replace(line.encode('utf-8'))
        words = line.split(';')
        wkey = words[0]
        dic[wkey] = [[],[]]
        zs = words[1].split(',')
        for i in range(len(zs)):
            dic[wkey][0].append(zs[i])
        ps = words[2].split(',')
        for i in range(len(ps)):
            dic[wkey][1].append(ps[i])
    
    
    xmldoc = minidom.parse('ccyplisting.xml')
    cells = xmldoc.getElementsByTagName('Data')
    out = open('WordsZhuPin.txt','w')
    fres = {}
    
    for cell in cells:
        data = cell.childNodes[0].nodeValue
        if hasChinese(data):
            words = data.split()
            for word in words:
                if hasChinese(word) and not fres.has_key(word):
                    zy = generateZhuPin(dic,word,0)
                    py = generateZhuPin(dic,word,1)
                    fres[word]=[zy,py]
    
    for key in fres.keys():
        r = key+";"+",".join(fres[key][0])+";"+",".join(fres[key][1])+'\n'
        out.write(r)
    
    out.close()

def generateZhuPin(dic, sentence, ztype):
    s = sentence.encode('utf-8')
    res = [""]
    for t in unicode(s):
        t = t.encode('utf-8')
        nres = []
        for r in res:
            if dic.has_key(t):
                for k in dic[t][ztype]:
                    nres.append(r+k)
            else:
                nres.append(r+t)
        res = nres
    return res
        
def replace(word):
    return re.sub('[" \n]', '', word)    

def hasChinese(content):
    iconvcontent = unicode(content)
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(iconvcontent)
    res = False
    if match:
        res = True
    return res

if __name__ == '__main__':
    main()