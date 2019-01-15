#修改电话号码
import xlrd
from xlutils.copy import copy

#打开一个work_book
xlsdoc = xlrd.open_workbook('E:/PythonProject/Python3/020/12.xls')
sheet = xlsdoc.sheet_by_index(0)
rows = sheet.nrows

#创建一个work_book的副本
cxlsdoc = copy(xlsdoc)
#通过副本get sheet
csheet = cxlsdoc.get_sheet(0)


#替换电话号码中的数字
for i in range(1,rows):
    phone = str(sheet.cell(i,5))
    #读取之后回添加text：这个字符串3
    phone = phone.replace('text:','')
    phone = phone.replace(phone[4:8],'****')
    csheet.write(i,5,phone)
    
    
cxlsdoc.save('E:/PythonProject/Python3/020/12.xls')