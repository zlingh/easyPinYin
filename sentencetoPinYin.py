# -*- coding:utf-8 -*-
import re
import os.path
def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

f1=open('inf.txt','r')
f2=open('outf.txt','w')
with open('word.json','r') as dtf:
    pydt=eval(dtf.readline())
newline=''
ish=0
for line in f1:
    line=line.decode('utf8')
    for c in line:
        if is_chinese(c):
            c=pydt[c]
            if ish==1:
                c='/'+c
            ish=1
        else:
            ish=0
        newline=newline+c
    newline=newline.encode('utf8')
    f2.write(newline)
    newline=''
f1.close()
f2.close()
