#encoding=utf-8
'''
Created on Oct 23, 2014

@author: Wu Xia
'''
import sys

def main():
    reload(sys)  
    sys.setdefaultencoding('utf8') 
    fn = sys.argv[1] #file_name
    f = open(fn,'r')
    out = open(sys.argv[2],'w')
    for line in f:
        line = line.encode('utf-8')
        words = line.split()
        r = words[0]+'\n'
        out.write(r.decode('utf-8'))
    
    f.close()
    out.close()


if __name__ == '__main__':
    main()