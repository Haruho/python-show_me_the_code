import redis

pool = redis.ConnectionPool(host = "localhost",port = 6379,db = 0)
#建立连接  需要先开启redis的服务端  这种连接方式是连接一次就断了  
#r = redis.Redis(host = "localhost",port = 6379,db = 0)
t = redis.Redis(connection_pool = pool)
print(t.dbsize())