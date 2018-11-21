#爬取图片
import urllib
import re
#获取网页源代码
def get_url():
    page = urllib.request.urlopen('http://tieba.baidu.com/p/2166231880')
    return page.read().decode('UTF-8')

#标签样式 不参与运行
mark = '<img pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C357%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C365/sign=408632710d3387449cc52f746134ba89/534906dfa9ec8a13d5853bc1f603918fa1ecc0dd.jpg" bdwater="杉本有美吧,1280,860" width="560" height="376" changedsize="true">'

#创建正则表达式来匹配相应的标签内的图片地址
reg = r'src="(.+?\.jpg)" bdwater'

#创建正则表达式的模式对象 省的重复转换模式
reg_img = re.compile(reg)
#用来给文件命名
index = 0
#返回下载进度
def downloadpercent(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    #计算下载的进度
    percent = 100.0 * a * b / c
    if percent>100:
        percent = 100
        print('下载完成')
    print('%.2f%%' % percent)

imglist = reg_img.findall(get_url())
print(imglist)
#下载图片
for i in imglist:
    index += 1
    #urlretrieve函数用来把那远程数据保存到本地
    urllib.request.urlretrieve(i,'E:/PythonProject/Python3/013/' + str(index)+'.jpg',downloadpercent)