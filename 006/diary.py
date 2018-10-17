#统计多个文本中出现频率高的词

import os
import re
diarypath = "E:/PythonProject/Python3/006/diary"

#需要忽略的词
#一般是介词  疑问词 代词  这里不一样输出结果大有不同
ignoreword = ['i','','he','a','at','in','of','for','an','be','are','she','his','him'
                'her','they','them','our','us','when','you','and',
                'what','why','how','the','with','to','"']
def getdiarycontent(dpath,filename):
    wordstimes = {}
    f = open(dpath,encoding = 'UTF-8')
    s = f.read()
    f.close()
    para = s.splitlines()
    for i in para:
        i.strip()
        words = re.split(r'[ ,.“”!]',i)
        for j in words:
            if j.lower() not in wordstimes.keys():
                wordstimes[j.lower()] = 1
            else:
                wordstimes[j.lower()] = wordstimes.get(j.lower()) + 1
    #print(wordstimes)  
    #处理出现频次
    #keyword = list(set(wordstimes.keys()).difference(ignoreword))
    for i in ignoreword:
        if(i in wordstimes):
            wordstimes.pop(i)
    #print(wordstimes)
  #  print(max(wordstimes,key = wordstimes.get))
    print(filename+'出现频率最高的词是：' + str(max(wordstimes,key = wordstimes.get)) + ",总共出现"+ str(wordstimes.get(max(wordstimes,key = wordstimes.get)))+'次')



#执行查找
for i in os.listdir(diarypath):
    getdiarycontent(os.path.join(diarypath,i),i)

