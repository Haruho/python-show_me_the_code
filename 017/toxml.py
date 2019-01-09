from xml.etree import ElementTree as ET
#存xls
import  xlwt
#读xls
import xlrd
#先把数据从xls中取出来
xlsdoc = xlrd.open_workbook('E:/PythonProject/Python3/017/student.xls')
#索引读取sheet
sheet = xlsdoc.sheet_by_index(0)
#根据名称读取sheet
#sheet = xlsdoc.sheet_by_name("name")
#根据索引获取一行的内容
#print(sheet.row_values(0))
#根据索引获取一列的内容
#print(sheet.col_values(0))
#获取行数和列数
# print('行数:' , sheet.nrows)
# print('列数:' , sheet.ncols)
#获取单元格的内容 第一行第二列
#cell = sheet.row(0)[1].value
def saveToXml(data):
    #根节点
    root = ET.Element('root')
    son = ET.SubElement(root,'student',{data.pop(0):data})
    tree = ET.ElementTree(root)
    tree.write('student.xml')

rows = sheet.nrows
for i in range(0,rows):
    l = sheet.row_values(i)
    #list
    #print(type(l),l)
    #pop返回被删除的元素
    #print(l.pop(0))
    saveToXml(l)