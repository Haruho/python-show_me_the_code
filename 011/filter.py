import os
import re

invaild = []
path = 'E:/PythonProject/Python3/011/filtered_words.txt'

temp = open(path,encoding = 'UTF-8').readlines()

#排除列表中‘/n’的影响
for i in temp:
    invaild.append(i.strip('\n'))

#print(invaild)
inputstr = input('输入任何文字')
if inputstr in invaild:
    print('Human Rights')
else:
    print('Freedom') 