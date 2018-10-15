#正则表达式

#re模块包含全部正则表达式的内容
import re


def REmatch():
    #re.match 按模式匹配字符串
    print(re.match("zch",'zchpython').span())
    print(re.match("zch",'pythonzch'))
    print(re.match(r'(.*) are (.*?) .*',"Cats are smarter thah dogs").span())
    #全字符匹配  .*  
    print(re.match(r'.* is .*','python is code').span())

def REsearch():
    print(re.search('zch','python zch').span())
    print(re.search('zch','zchpython').span())
    print(re.search('zch','asdfghjklzc'))
    #search也能全字符匹配
    print(re.search(r'.* is .*','issca is fun').span())
def REsub():
    #检索和替换
    phone = "phonenumber # 000-0000-0000"
    num = re.sub(r'.*#','',phone)
    #\D代表所有非数字字符
    num = re.sub(r'\D','',phone)
    print(num)

def REcompile():
    #匹配一个正则表达式，包含match和search函数
    pattern = re.compile(r'\d+')
    #从第二个元素开始匹配
    print(pattern.match("q2werty",1,4))
    print(pattern.match("1qweasd"))
    print(pattern.search('zxcasdqwe4asdasd'))


def REsplit():
    #多个分隔符写法
    s = 'a,b-c^d e'
    lines = """a b c 
                d e"""
    #1.分隔符之间用  |  来分开  有部分符号需要使用转义 ‘|\分隔符’  向下面的^符号
    print(re.split(r'-|,|\^| ',s))
    #2.使用[]
    print(re.split(r'[-,^ ]',lines))
REsplit()