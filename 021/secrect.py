#加密
import hashlib

a = 'Hello World'

#system中支持的所有加密算法
# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

#MD5
#b把string转换成bytes
hash_object = hashlib.md5(b'Hello World')
#print(hash_object.hexdigest())

#SHA1
hashsha1 = hashlib.sha1(b'Hello World')
print(hashsha1.hexdigest())

#函数一样  包括sha224  256  384  512

