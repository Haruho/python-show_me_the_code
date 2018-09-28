#获取随机元素
import random

from xml.etree import ElementTree as ET
import json
import xlwt
def generate_ticket():
    a = "abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    temp = random.sample(a,16)
    ticket = "".join(temp)
    return ticket

#用xml存
def saveCodeByXml():
    #根节点
    root = ET.Element('code')
    #按需生成
    for i in range(0,10):
        son = ET.SubElement(root,'code'+str(i),{'ticket':generate_ticket()})
    #创建文件
    tree = ET.ElementTree(root)
    tree.write('saveByxml.xml')
#用json存
def saveCodeByJson():
    jsonData = {}
    for i in range(0,10):
        jsonData.update({'code' + str(i+1):generate_ticket()})
    #生成json的str   添加排序和缩进  美化json格式
    data = json.dumps(jsonData,sort_keys=True,indent=4)
    jsonfile = open("saveByJson.json",'w')
    jsonfile.write(data)
    jsonfile.close()
#用表格存
def saveCodeByExcle():
    wbk = xlwt.Workbook()
    #创建sheet
    sheet = wbk.add_sheet("优惠券")
    #在第一行第二列的单元中写 test text
    #注意表格的序号是从0开始
    #sheet.write(0,1,"test text")
    for i in range(0,10):
        sheet.write(i,0,'code'+ str(i+1))
        sheet.write(i,1,generate_ticket())
    wbk.save("saveByExcle.xls")


saveCodeByXml()
saveCodeByJson()
saveCodeByExcle()