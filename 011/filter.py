import os
import re

invaild = []
path = 'E:/PythonProject/Python3/011/filtered_words.txt'

temp = open(path,encoding = 'UTF-8').readlines()
endresult = ''
#排除列表中‘/n’的影响
for i in temp:
    invaild.append(i.strip('\n'))

inputstr = str(input('输入任何文字'))


def combainresult(sentence):
    for i in invaild:
        if i in sentence:
            #回调
            combainresult(sentence.replace(i,'**'))
            #结果赋值
            sentence = sentence.replace(i,'**')
    return sentence

print(combainresult(inputstr))