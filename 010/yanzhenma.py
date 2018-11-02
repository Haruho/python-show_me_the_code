#生成一个验证码图片

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
#不是从基础图片上改的
#是一步一步创建出来的


image = Image.new('RGB',(150,30),'red')

#给图片添加文字
#获取一个画笔对象
draw = ImageDraw.Draw(image)
#获取一个font对象
font = ImageFont.truetype('calibril.ttf',size=40)
#写字   能不能改字间距？  想要文字居中？
draw.text((35,0),'1234',(255,255,255),font=font)
#添加噪点和噪线
width = 150
height = 30
#draw line
for i in range(5):
    x1 = random.randint(0,width)
    x2 = random.randint(0,width)
    y1 = random.randint(0,height)    
    y2 = random.randint(0,height)
    draw.line((x1,y1,x2,y2),fill=(255,255,255))   
#画点
for i in range(300):
    draw.point([random.randint(0,width),random.randint(0,height)],fill= (255,255,255))
    x = random.randint(0,width)
    y = random.randint(0,height)
    draw.arc((x,y,x+4,y+4),0,90,fill=(255,255,255))
#生成一个名为test的png图片文件
image.save(open('test.png','wb'),'png')
