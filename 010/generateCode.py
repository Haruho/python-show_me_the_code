#生成
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

strList = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
#创建随即颜色
def getRandomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

#获取一个随即的字符串
def getRandomText():
    return ''.join(random.sample(strList,4))

#创建一张图片
captcha = Image.new('RGB',(150,50),getRandomColor())
#填写验证码
font = ImageFont.truetype('calibriz.ttf',size=35)
#print(font.getsize(getRandomText()))
draw = ImageDraw.Draw(captcha)
#text没提供旋转的方法
draw.text((40,10),getRandomText(),fill = getRandomColor(),font=font)
#添加线
for i in range(5):
    draw.line((random.randint(0,150),random.randint(0,30),random.randint(0,150),random.randint(0,50)),fill=getRandomColor())

#画点
for i in range(300):
    draw.point((random.randint(0,150),random.randint(0,30),random.randint(0,150),random.randint(0,50)),fill=getRandomColor())
captcha.save('E:/PythonProject/Python3/010/captcha.png','png')