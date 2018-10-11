#把生成的激活码存在redis中
#激活的特性有三个   id content state
#第一反应应该是hash
#或者三个set  
#三个set操作起来也太麻烦了

import redis
import generatekey.getRandom


pool = redis.ConnectionPool(host = 'localhost',port = 6379,db = 2)

r = redis.Redis(connection_pool=pool)


#这个写法会导致每次连接更新的时候就把数据给更新了
# def saveKey():
#         for i in range(0,11):
#                 r.hmset('key',{'id':i,"content":generatekey.getRandom.generate_ticket(),'state':0})

#每次执行之前先清空一下key
# r.delete('key')

# def saveKey(i):
#         r.hset('key','id',i)
#         r.hset('key','content',generatekey.getRandom.generate_ticket())
#         r.hset('key','state',0)

# for i in range(0,11):
#         saveKey(i)

#我可能理解错了hash的结构

# print(r.hlen('key'))
# for i in range(0,11):
#         print(r.hmget('key','id','content','state'))
#hash的结构是  key filed1 value   filed2 value  value
#我上面被注释掉的操作都是在操作的同一个hash  按照上面的想法   应该是hash里面嵌套hash才对
#学艺不精丢人了

def saveKey():
        for i in  range(0,11):
                r.hmset("key"+str(i),{'id':i,'content':generatekey.getRandom.generate_ticket(),"state":0})


for i in range(0,11):
        print(r.hmget('key'+str(i),'id','content','state'))



#用string   sets都能存  list就不太好了