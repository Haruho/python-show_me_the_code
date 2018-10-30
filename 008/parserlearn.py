from html.parser import HTMLParser

htmlstr = '''<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
        <img src = "" />
        <p>A paragraph.</p>
                <p class = "p_font">A paragraph with class.</p>
                <!-- comment -->
        <div>
            <p>A paragraph in div.</p>
        </div>
    </body>
</html>'''

#继承HTMLParser  重写方法
class Myparser(HTMLParser):
    #处理开始标签
    def handle_starttag(self,tag,attrs):
        return
        print(tag,'--',attrs)

    #处理结束标签
    def handle_endtag(self,tag):
        return
        print(tag)
    
    #处理标签里的内容
    def handle_data(self,data):
        return
        print(data)

    #处理开始和结束标签闭合的标签
    def handle_startendtag(self,tag,attrs):
        return
        print(tag,'--',attrs)

    #处理注释
    def handle_comment(self,data):
        return
        print(data)

    #处理全部p标签
    def handle_data(self,data):
        return
        #lasttag表示上一次操作的标签
        if self.lasttag == 'p':
            print(data)


    in_div = False
    #处理div标签下的p标签
    def __init___(self):
        HTMLParser.__init__(self)
        self.in_div = False

    def handle_starttag(self,tag,attrs):
        if tag == 'div':
            self.in_div = True

    def handle_data(self,data):
        if self.in_div == True and self.lasttag == 'p':
            print(data)

#创建实例
parser = Myparser()
#添加html
parser.feed(htmlstr)