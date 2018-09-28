#Pillow库的使用
from PIL import Image
#打开
im = Image.open("face.jpg")
#旋转
im.rotate(45).show()