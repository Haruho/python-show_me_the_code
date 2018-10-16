#PIL image简单操作
from PIL import Image
import os
# #open  打开图片
# im = Image.open('E:/PythonProject/Python3/005/pythonimage/1.jpg')
# #size属性表示图片大小  是一个元祖
# size = 1800,1080
# #缩略图  不能变大
# im.thumbnail(size,Image.ANTIALIAS)
# #试验之后发现这个也不能变大
# #im.resize(size,Image.ANTIALIAS)
# im.save('E:/PythonProject/Python3/005/pythonimage/1thum.jpg',"JPEG")
path = 'E:/PythonProject/Python3/005/pythonimage'
def readimagefiles():
    #返回文件名
    for i in os.listdir(path):
        #返回文件路径
        pathname = os.path.join(path, i)
        print(pathname)
    #返回一个str list list形式的元祖（文件根目录，[文件夹名]，[文件名]）
    for j in os.walk(path):
        #pathname = os.path.join(path, j)
        print(j)

readimagefiles()