#读取特定格式的txt文件并把数据转存成表格

import xlwt
import json
#txt文本和json格式类似
t = open('E:/PythonProject/Python3/015/city.txt',encoding = 'utf-8')
jsonstr = t.read();
#dict
js = json.loads(jsonstr)


def savetoxls():
    file = xlwt.Workbook()
    sheet = file.add_sheet('City')
    # sheet.write(0,0,'1')
    # sheet.write(1,0,'2')
    # sheet.write(2,0,'3')
    # sheet.write(0,1,js.get("1"))
    # sheet.write(1,1,js.get("2"))
    # sheet.write(2,1,js.get("3"))
    #改进版本
    for i in range(0,3):
        #1列
        sheet.write(i,0,list(js.keys())[i])
        #2列
        sheet.write(i,1,list(js.values())[i])        
    file.save('E:/PythonProject/Python3/015/city.xls');

savetoxls()
