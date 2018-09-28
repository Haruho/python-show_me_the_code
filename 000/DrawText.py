from PIL import Image,ImageDraw,ImageFont
im = Image.open("face.jpg")
drawtext = ImageDraw.Draw(im)

# drawtext.text((0,0),"12",fill=120)
font1 = ImageFont.truetype("calibri.ttf",30)

#如何修改text的size
drawtext.text((im.size[0] - 30,0),"12",font = font1,fill=120)

im.save("first1.png","png")

# print(im.size[0])