#统计字符串
import os
import re
#按照格式打开
f = open('standradText.txt',encoding ="UTF-8")

s = f.read()
f.close()
#按照行先分割一下
para = s.splitlines()
paranospace = []
wordict = {}
test = []
for i in para:
    i.strip()
    #所有的分隔符  这个需要仔细查找
    cutpara = re.split(r'[,. !“”?]',i)
    test = cutpara
   # print(cutpara)
    for j in cutpara:
        if(j is not ''):
            #判断这个单词处没出现过  不计空格 转换大小写
            if(j.lower() not in wordict.keys()):
                wordict[j.lower()] = 1
            #再次遇到相同的次就把value+1
            else:
                wordict[j.lower()] = wordict.get(j.lower()) + 1

# for i in wordict:
#     print(i +'  出现的次数是：'+ str(wordict.get(i)))