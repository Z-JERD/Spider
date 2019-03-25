html_doc = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>睡鼠的故事</title>
        </head>
    <body>
        <p class ="title">
            <b>睡鼠的故事</b>
        </p>
        <p class ="story">从前有三个小姐妹; 他们的名字是
            <a href="http://example.com/elsie" class="sister" id="link1"> Elsie </a>和
            <a href =“http://example.com/lacie" class ="sister" id ="link2"></a>
            <a href="http://example.com/tillie" class="sister" id="link3">Title</a>;他们住在井底。
        </p>

        <p class ="story">
        ...
        </p>
"""

#BeautifulSoup库#
"""
BeautifulSoup库是解析，遍历，维护"标签树"的功能库
1. pip install beautifulsoup4
2.解析器
Python的html.parser  BeautifulSoup(markup, "html.parser")
第三方Python解析器：
    1.pip install lxml
        lxmlHTML解析器  BeautifulSoup(markup, "lxml")  推荐使用,速度快
        lxml的XML解析器 BeautifulSoup(markup, "lxml-xml")
                        BeautifulSoup(markup, "xml")
    2.html5lib解析器，它以Web浏览器的方式解析HTML
     pip install html5lib
     BeautifulSoup(markup, "html5lib")

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
soup=BeautifulSoup(r1.text,"html.parser")
print(soup.prettify())  显示完整的html代码  嵌套数据结构
html.parser是python用来解析html的模块。它可以分析出html里面的标签、数据等等，是一种处理html的简便途径

"""

#BeautifulSoup的用法#
"""
1.soup.prettify() 将文档表示为嵌套数据结构,字符串类型的标签
2.soup.tag
    soup.find("div")
    soup.find(name="div",attrs={"id":"zhao"})
    返回匹配结果的第一个值 name放标签名,attrs放属性值
3.soup.find_all  查到所有的标签，值为列表
    1.name参数
        soup.find_all('b')  
    2.关键字参数
        soup.find_all(href=re.compile("elsie"),id='link2') 
        等同于soup.find_all(attrs={"href":re.compile("elsie"),"id":"link2"}) 
    3.按CSS类搜索
        soup.find_all("a", class_="sister") 
        soup.select("p.strikeout.body")搜索与两个或更多CSS类匹配的标记
    4.使用其search()方法过滤该正则表达式
        soup.find_all(re.compile("t"))   查到有b的标签 html title
    5.list列表
        soup.find_all(["a", "b"]) 查到所有的a标签b标签所有的标签
    6. soup.find_all(True) 找到
    7.自定义函数：
        def has_class_but_no_id(tag):  
            return tag.has_attr('class') and not tag.has_attr('id')
        soup.find_all(has_class_but_no_id)
        def not_lacie(href):
            return href and not re.compile("lacie").search(href)
        soup.find_all(href=not_lacie)
    8.string参数
        soup.find_all(string="Elsie") 查找文本
        soup.find_all("a", string/text="Elsie") 查找到文本时候Elsie的a标签
    9.limit参数
        soup.find_all("a", limit=2)
3.soup.text/soup.get_text() 获取所有的文本值 有空格
    soup.tag.strings 获取所有的文本值返回值生成器 有很多额外的空格 
    soup.tag.strings 删除空格
    for string in soup.stripped_strings:
        print(repr(string))  #将空格以"\n"的形式展示
    
    soup.tag.string  #显示标签中的文本内容
4.soup.tag.get('href')/ soup['href'] 获取属性值
5.soup.tag.parent  父标签   soup.tag.string.parent 文本的父标签是当前标签
  soup.tag.parents 父辈 返回值是生成器
  soup.tag.contents 子标签,结果是list
  soup.tag.children  返回生成器
  soup.tag.string
6.soup.tag.next_sibling 同一级别的下一个元素  支持soup.tag.next_sibling.next_sibling
  soup.tag.previous_sibling 同一级别的上一个元素
    <a href=""id="link2"></a>他们住在井底<a href="" id="link3">在井底。</a>
    print(soup.a.next_sibling) #他们住在井底
7.soup.next_element  标签中有文本,值为文本，无文本 值为下个元素
  soup.previous_element
    <a href="" id="link3"></a>他们住在井底      #他们住在井底
    <a href="" id="link3">Title</a>他们住在井底  #Title
    <a href="" id="link2"></a><a>Title</a> #<a>Title</a>
8.oup.tag.name
9.soup.tag.attrs 当前标签的属性值 #{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
  class是多值属性，值为列表
  使用`get_attribute_list获取始终为列表，字符串的值，无论它是否为多值属性
  id_soup.p.get_attribute_list（'id'）＃[“我的id”]
  如果将文档解析为XML，则不存在多值属性：
10.tag.string.replace_with(value) 替换字符串
11.soup.tag.has_attr('id') 判断标签是否有某个属性
"""

from bs4 import BeautifulSoup
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup = BeautifulSoup(html_doc,"html.parser")
print(soup.find_all(has_class_but_no_id))

#用法实例：
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")
#print(soup.prettify())
#print(soup.title,type(soup.title)) #显示匹配到的第一个标签 <class 'bs4.element.Tag'>
#print(soup.p.name,type(soup.p.name)) #显示标签的名称 <class 'str'>
#print(soup.title.string) #显示标签中的文本内容
#print(soup.title.parent) #显示当前标签的父标签
#print(soup.p['class']) #显示当前标签的属性的值 值为列表 ['title']
#print(soup.find_all(name='a',attrs={'class':"sister"})) #查到所有的标签，值为列表
#print(soup.find('a'))   #返回匹配结果的第一个
#print(soup.get_text())
# for link in soup.find_all('a'):
#     print(link['href'])
"""



