#处理text文件
import os
import re
#工程目录
f = open('text.txt','rb')

s = f.read()

f.close()

#简单的切割字符串
print(s.split(" ")) 

#多行切割
print(s.splitlines())


# #print(paranospace)
# s = 'a a aaa,b bb bb.c c cc'
# words = re.split(r'[ ,.]',s)
# #print(words)
# timesdict = {}
# for i in words:
#     if i not in timesdict.keys():
#         timesdict[i] = 1
#     else:
#         timesdict[i] = timesdict.get(i) + 1




# for i in timesdict:
#     print(i+'出现的次数是：' + str(timesdict.get(i)))