#把所有生成的激活码上传到数据库
import pymysql
import generatekey.getRandom


key = []
for i in range(0,10):
    key.append(generatekey.getRandom.generate_ticket())

def saveKeyToDB():
    connection = pymysql.connect(host = "localhost",user = "root",password="123456",db= "MySchema")
    cursor = connection.cursor()
    for i in range(0,len(key)):
        #sql = "INSERT INTO ACTIVEKEY(ID,CONTENT,STATE)  VALUES('%i','%c','%s')" %(int(i),key[i],0)
        sql = "INSERT INTO ACTIVEKEY(ID,CONTENT,STATE)  VALUES({},'{}',{})".format(i,key[i],0)
        try:
            cursor.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            connection.close()

saveKeyToDB()