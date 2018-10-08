#将上一题的数据存到mysql关系型数据库中
#先连接数据库
import pymysql

def getMysqlVersion():
    #创建连接   参数分别是 1.MySQL Connection的名字 或者地址  2.使用数据库的用户名  3.用户密码 4.数据库名
    db = pymysql.connect("localhost","root","123456","MySchema")
    #创建一个游标
    cursor = db.cursor()
    #执行MySQL语句
    cursor.execute("SELECT VERSION()")
    #fetchone 获取单条数据
    data = cursor.fetchone()
    print("data: %s" % data)
    #关闭数据库连接
    db.close()



def creatConnection():
    connection = pymysql.connect(host = "localhost",user = "root",password = "123456",db="MySchema")


def createTable():
    #建立连接
    connection = pymysql.connect(host = "localhost",user = "root",password = "123456",db="MySchema")
    cursor = connection.cursor()
    #执行mysql的语句  如果存在ACTIVEKEY这个表  那么先删除这个表
    cursor.execute("DROP TABLE IF EXISTS ACTIVEKEY")
    #创建表 并且输入每列的记录名称  格式（长度） 特殊属性
    sql = """CREATE TABLE ACTIVEKEY(
        ID VARCHAR(45) NOT NULL PRIMARY KEY,
        CONTENT VARCHAR(45) NOT NULL,
        STATE TINYINT(4) NOT NULL
    )"""
    #执行上面的语句
    cursor.execute(sql)
    connection.close()

#插入数据
def insertdata():
    #建立连接
    connection = pymysql.connect(host = "localhost",user = "root",password = "123456",db="MySchema")
    cursor = connection.cursor()
    #插入数据的sql语句
    sql = """INSERT INTO ACTIVEKEY(ID,CONTENT,STATE)
    VALUES('0','qwerqwerqwer','0')"""
    try:
        cursor.execute(sql)
        #提交数据库执行
        connection.commit()
    except:
        #如果发生了错误则回滚
        connection.rollback()
        connection.close()


#查询数据
def selectData():
    connection = pymysql.connect(host = "localhost",user ="root",password="123456",db = "MySchema")
    cursor = connection.cursor()
    sql = "SELECT content FROM ACTIVEKEY"
    try:
        cursor.execute(sql)
        #获取返回的结果是一个元祖
        result = cursor.fetchall()
        #print(type(result))
        print(result)
    except:
        print("fetch data fail")
        connection.close()


#修改数据
def changeData():
    connection = pymysql.connect(host = "localhost",user = "root",password = "123456",db = "MySchema")
    cursor = connection.cursor()
    #把所有的id都+1  更新的关键字是Update
    sql = "UPDATE ACTIVEKEY SET CONTENT = "12902"
    try:4
        cursor.execute(sql)
        connection.commit()
    except:
        connection.rollback()
        connection.close()

