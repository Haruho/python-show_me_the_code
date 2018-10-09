#连接非关系型数据库Redis
import redis

pool = redis.ConnectionPool(host = "localhost",port = 6379)
#建立连接  需要先开启redis的服务端
#r = redis.Redis(host = "localhost",port = 6379,db = 0)
r = redis.Redis(connection_pool = pool)
#添加一条数据
r.set("country","China")
#获取country的value
print(r.get("country"))
#同上
print(r['country'])
#返回keys
print(r.keys())
print(r.dbsize())