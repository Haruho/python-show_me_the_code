#修改图片的size小于iphone5的分辨率
from PIL import Image
import os
path = 'E:/PythonProject/Python3/005/pythonimage'
#size  
size = 1136,640

def walkfiles():
    for i in os.listdir(path):
        #过滤文件和目录如果需要判断文件是不是图片的话就需要检测后缀
        if(os.path.isfile(os.path.join(path,i))):
            #print('Path是：' + os.path.join(path,i) + '  name是：' + i)
            thumbnailimage(os.path.join(path,i),i)

def thumbnailimage(imgpath,name):
    im = Image.open(imgpath)
    #当给定的size大于图片本身的size 则不会生成缩略图
    im.thumbnail(size,Image.ANTIALIAS)
    #这里重命名文件名  用join也能修改格式 哪种方式都一样
   # print(path+'/'+name.replace('.jpg','_thum.jpg'))
    im.save(path+'/'+name.replace('.jpg','_thum.jpg'),'JPEG')

walkfiles()