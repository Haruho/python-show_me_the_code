from PIL import Image
import os

path = 'E:/PythonProject/Python3/022/pythonimage'

size_height = int(input('请输入高'))
size_weight = int(input('请输入宽'))

size = size_height,size_weight
def walkfiles():
    for i in os.listdir(path):
        if(os.path.isfile(os.path.join(path,i))):
            thumbnailimage(os.path.join(path,i),i)


def thumbnailimage(imgpath,name):
    im = Image.open(imgpath)
    #当给定的size大于图片本身的size 则不会生成缩略图
    im.thumbnail(size,Image.ANTIALIAS)
    #这里重命名文件名  用join也能修改格式 哪种方式都一样
   # print(path+'/'+name.replace('.jpg','_thum.jpg'))
    im.save(path+'/'+name.replace('.jpg','_thum.jpg'),'JPEG')

walkfiles()