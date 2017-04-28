# coding: utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
i_dict = {}
file = open('/home/cu/Desktop/太空旅客.txt','r')
goalfile = file.readlines()

for p,dirs,files in os.walk('/home/cu/Desktop/词典'):
    for f in files:
        # print os.path.join(p,f)
        with open(os.path.join(p,f)) as f:
            for line in f:
                i_dict[line.decode("utf-8","ignore").strip()] = 0

for lines in goalfile:
    for k in i_dict:
        if k in lines:
            i_dict[k] = i_dict[k] +1

with open('/home/cu/关注点.txt','w')as f2 :   #新建一个文本，把结果录入文本文件中
    for k in i_dict:
        f2.write(k)
        f2.write(" ")
        f2.write(str(i_dict[k]))
        f2.write('\n')

