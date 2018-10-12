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