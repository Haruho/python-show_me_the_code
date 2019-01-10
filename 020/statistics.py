#统计通话记录
#保护隐私
import xlrd

xlsdoc = xlrd.open_workbook('E:/PythonProject/Python3/020/record.xls')

sheet = xlsdoc.sheet_by_index(0)
#shoujihao
colv = sheet.col_values(5);
