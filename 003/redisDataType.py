#python操作redis的各种数据类型
import redis

pool = redis.ConnectionPool(host = "localhost",port = 6379,db = 0)
#建立连接  需要先开启redis的服务端  这种连接方式是连接一次就断了  
#r = redis.Redis(host = "localhost",port = 6379,db = 0)
r = redis.Redis(connection_pool = pool)
#string类型
def stringDataType():
    #单个数据的存储
    # r.set("name","zch")
    # r.set('name','nzch')
    # print(r.get("name"))
    # print(r.get("country"))
    #多个数据存储
    r.mset({'age':12,'sex':"male"})
    #向数据的值中添加字符
    r.append('age',0)
    print(r.get("age"))
    print(r.get("sex"))
    #输出一段值
    print(r.getrange("sex",0,0))

#hash类型
def hashDataType():
    #单词存入
    r.hset('Animal','miaoli','cat')
    r.hset('Animal','weilai','cat')
    r.hset('Animal','eryue','dog')
    #一次存多个
    r.hmset("Car",{'toyota':'janpan','byd':'china','ford':'usa'})
    print(r.hmget('Car',['toyota','byd','ford']))
    print(r.hget('Animal','miaoli'))
    print(r.hget('Animal','weilai'))
    print(r.hget('Animal','eryue'))

#list类型
def listDataType():
    #left push ,所以这时候列表的元素顺序是  b-a-o  返回值是int 代表列表长度    
    a = r.lpush("fruit","orange","apple","banana")
    #right push添加元素到右边，所以这个是添加之后，添加元素的顺序不变
  #  r.rpush('fruit','pear','plum')
    #移除元素
  #  r.lrem('fruit','orange',5)
    #修剪list   删除参数范围外的所有元素
    r.ltrim('fruit',5,8)
    # r.lrem('fruit','apple',0)
    # r.lrem('fruit','banana',0)
    print(r.lrange('fruit',0,r.llen('fruit')))


#集合数据类型  不允许重复的list
def setDataType():
    #添加元素
    r.sadd('key1','a','b','c')
    r.sadd('key2','c','d','e')
    #查询长度
    #print(r.scard('key1'))
    #key1和key2的差集
    print(r.sdiff('key1','key2'))
    #交集
    print(r.sinter('key1','key2'))
    #并集
    print(r.sunion('key1','key2'))
    #确定一个值是不是set中的元素
    print(r.sismember('key1','a'))
    print(r.sismember('key1','f'))
    #获取集合中所有元素  返回一个set类型的数据
    print(r.smembers('key1'))
    #删除
    r.srem('key2','d')
    print(r.smembers('key2'))

#有序集合   排了顺序的集合
def storesetDataType():
    r.zadd('zset',"one",1)
    r.zadd('zset',"two",2)
    r.zadd('zset',"three",3)
    #r.zadd('zset',5,'five')

storesetDataType()

r.zrem('zset','two')
print(r.zrangebyscore('zset',0,10))