import xlwt
import re
t = open('E:/PythonProject/Python3/016/numbers.txt',encoding = 'utf-8')

s = t.readlines()

#txt文本不能直接操作  需要进行一些操作把数据提炼出来
file = xlwt.Workbook()
sheet = file.add_sheet("numbers")
k = 0
for line in s:
    #print('item:  ' + line)
    if '[' in line:
        if ']' in line:
            #获取所有的数据  
            #去掉转义字符
            line = line.strip('\n\t')
            #把 [ ] ,去掉
            line = line.replace('[','')
            line = line.replace(']','')
            line = line.replace(',','')
            #从空格开始拆分字符串  返回list
            l = re.split(' ',line)
            print(l)
            for i in range(0,len(l)):
                sheet.write(k,i,l[i])
            k += 1
            

file.save('E:/PythonProject/Python3/016/number.xls');