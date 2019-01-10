#Learning is noending...
import xlrd
import xml.etree.ElementTree as etree

#打开xls
xlsdoc = xlrd.open_workbook('E:/PythonProject/Python3/018/city.xls',encoding_override='utf-8')
#获取sheet
sheet = xlsdoc.sheet_by_index(0)
#获取行数 列数
row = sheet.nrows
col = sheet.ncols

#所有数据
alldata = {}
for i in range(0,row):
    l = sheet.row_values(i)
    alldata[l[0]] = l[col-1]

#注释内容
comment = etree.Comment('城市信息')
#创建根节点
root = etree.Element('root')
#插入注释
root.insert(1,comment)
#创建子节点
son = etree.SubElement(root,'city')
#写入数据
son.text = str(alldata)
#创建tree
xmldoc = etree.ElementTree(root)
xmldoc.write('E:/PythonProject/Python3/018/city.xml',encoding='utf-8',xml_declaration=True)