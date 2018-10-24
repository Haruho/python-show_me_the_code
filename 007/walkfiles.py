#先看看能不能遍历到所有的py文件

import os
import re
path = 'E:/PythonProject/Python3/'

pyfiles = []
#输出全是转义字符
# for i in os.listdir(path):
#     r = open(os.path.join(path,i),'rb')
#     print(r.read())

for i in os.walk(path):
    if('.' not in i[0]):
        #所有目录地址
        #print(i[0])
        #所有的文件夹
        #print(i[1])
        #所有的文件
        #print(i[2])
        for j in i[2]:
            if(j[-3:] == '.py'):
                pyfiles.append(i[0] +'/'+ j)
                


#print(pyfiles)
#截取字符串
# print('123456'[-3:])
#下面的三个列表用来存储所有line和注释和空行
lines = []
nullline = []
noteline = []
def countlines(filepath):
    r = open(filepath,encoding = 'utf-8')
    for i in r.readlines():
        #清除行数左边的空格  方便进行判断
        i.lstrip()
        #获取上所有行
        lines.append(i)
        #开头是#的就是注释
        if i[0] == '#':
            noteline.append(i)
        #匹配换行
        if i == '\n':
            nullline.append(i)
for i in pyfiles:
    #输出文件名
    print('这些文件是',i[25:])
    countlines(i)

#print(lines)
print('所有代码一共有  ' , len(lines))
print('语句一共有' ,len(lines) - len(noteline) -len(nullline))
print('注释一共有 ' , len(noteline))
print('空行一共有 ' ,len(nullline))
