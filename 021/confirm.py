#验证密码
#设密码是  11223344
import hashlib

method = 'SHA1'
#存密码的时候掉用这个  然后把结果存在db中
def passwordsafty(password):
    content =  hashlib.sha1((method + password).encode())
    return content.hexdigest()
    

def cheakpassword(password):
    #应该从db中获取sha1的hash  对比hash返回是否
    scontent = hashlib.sha1((method + password).encode())
    print( passwordsafty(password) == scontent )

x = input(str('请输入密码'))

cheakpassword(x)