import xml.etree.ElementTree as etree
import xlrd

xlsdoc = xlrd.open_workbook('E:/PythonProject/Python3/019/number.xls')
sheet = xlsdoc.sheet_by_index(0)

row = sheet.nrows
col = sheet.ncols

alldata = []
for i in range(0,row):
    l = sheet.row_values(i)
    alldata.append(l)


comment = etree.Comment('数字信息')
root = etree.Element('root')
root.insert(1,comment)
son = etree.SubElement(root,'numbers')
son.text = str(alldata)
xmldoc = etree.ElementTree(root)
xmldoc.write('E:/PythonProject/Python3/019/number.xml',encoding='utf-8',xml_declaration=True)