#连接非关系型数据库Redis
import redis
#连接池  这个方式会一次性创建很多连接，每次执行连接操作的时候，就在这个pool中取出一个连接来使用
pool = redis.ConnectionPool(host = "localhost",port = 6379)
#建立连接  需要先开启redis的服务端  这种连接方式是连接一次就断了  
#r = redis.Redis(host = "localhost",port = 6379,db = 0)
r = redis.Redis(connection_pool = pool)
#添加一条数据
r.set("country","China")
#获取country的value
print(r.get("country"))
#同上6
print(r['country'])
#返回keys
print(r.keys())
print(r.dbsize())