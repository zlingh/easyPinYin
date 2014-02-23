# -*- coding:utf-8 -*-
dt=eval(open('word.json','r').readline())
s=u'用一句代码导入字典，将汉字转换为拼音，简单明白'
pys=''
for k in s:
    if k not in dt:
        pys+=k
    else:
        pys=pys+dt[k]+' '
pys=pys.strip()
print pys
