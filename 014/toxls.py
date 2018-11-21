import json
import xlwt
t = open('E:/PythonProject/Python3/014/student.txt',encoding = 'utf-8')
jsonstr = t.read()
#print(jsonstr)
#使用loads函数把jsonstr转换成dict类型数据
js = json.loads(jsonstr)
#dict类型
#print(type(js))
print(js)
#乱码
#print(json.dumps(js))
#正常显示中文
#print(json.dumps(js,ensure_ascii=False))

#把字典转换成list  第一个元素是key 之后是values
def remakedict(key):
    temp = []
    temp.append(key)
    for i in js.get(key):
        temp.append(i)
    return temp

def chagetoxls():
    file = xlwt.Workbook()
    sheet = file.add_sheet('成绩单')
    for i in  range(0,5):
        sheet.write(0,i,remakedict('1')[i])
        sheet.write(1,i,remakedict('2')[i])
        sheet.write(2,i,remakedict('3')[i])
    file.save("E:/PythonProject/Python3/014/student.xls")

chagetoxls()