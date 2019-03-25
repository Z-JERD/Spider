# requests模块的应用#
"""
HTTP 请求类型：GET,PUT，DELETE，HEAD 以及 OPTIONS
r = requests.get(url)
r = requests.post(url,data = {'key':'value'})
r = requests.put(url,data = {'key':'value'})
r = requests.delete(url,)
r = requests.head(url)
 r = requests.options(url)
"""
# GET请求#
"""
1.url
2.params 
    1.关键字参数:字典里值为 None 的键不会添加到url中
        payload = {'key1': 'value1','key2': 'value2'}
        r = requests.get(url,params = payload)  
        print(r.url) # url?key1=value&key2=value2
    2.将一个列表作为值传入
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
     url?key1=value&key2=value2&key2=value3
3.headers 请求头
     headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    }


"""
# POST请求#
"""
1.data 和 json 传递数据
    chrome: 请求体的类型是formdata时用data
       payload = {'key1': 'value1', 'key2': ['value2','value3']}
       url = "http://httpbin.org/post"
       r = requests.post(url, data=json.dumps(payload))
    chrome: 请求体的类型是payload 时用json
        r = requests.post(url, json = payload)  
2.传递一个 string
    r = requests.post(url, data=json.dumps(payload))
3.files  传送文件类型
    url = 'http://httpbin.org/post'
    files = {'file': open('log.txt', 'rb')}
    r = requests.post(url, files=files)
4.发送cookie
    cookies = dict(cookies_are='working')
    r = requests.get(url, cookies=cookies)
    Cookie 的返回对象为 RequestsCookieJar 适合跨域名跨路径使用
    import requests
    import json
    jar = requests.cookies.RequestsCookieJar()
    jar.set('key1', 'value1')
    jar.set('key2', 'value2')
    url = 'http://httpbin.org/cookies'
    r = requests.get(url, cookies=jar)
    print(r.text)
5.禁用重定向处理
    除了 HEAD, Requests会自动处理所有重定向
    get/post请求禁用重定向： r = requests.get(url, allow_redirects=False)
    启用重定向:r = requests.head(url, allow_redirects=True)
6.超时设置：停止等待响应,代码都应该使用这一参数
    requests.get(url, timeout=0.001) timeout 仅对连接过程有效
"""

# 响应#
"""
requests对象都会返回一个Response对象，
这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等
响应：
    1.r1.headers  头信息
    2.r1.status_code HTTP请求的返回状态码 200表示成功
        内置的状态码查询对象 r.status_code == requests.codes.ok
        如果请求错误：通过 Response.raise_for_status() 来抛出异常
    3.r1.encoding:从HTTP header猜测的内容编码方式
        如果header中不存在charset字段，默认编码为ISO-8859-1，此时的编码输出r.text中的中文将是乱码。
    4.r1.apparent_encoding:会根据HTTP网页的内容分析出应该使用的编码。
    5.r1.cookies.get_dict()  取到cookies值
    6.r1.content  HTTP响应内容的二进制形式(存的是字节码) 用于非文本请求
    7.r1.text 	HTTP响应内容的字符串形式
    8.r1.json()    处理 JSON 数据 如果 JSON 解码失败， r.json() 就会抛出一个异常
    9.r.raw 原始套接字响应 对象列表按照从最老到最近的请求进行排序
    10.r.history 请求历史
    11.错误与异常
        遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
        如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
        若请求超时，则抛出一个 Timeout 异常。
        若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
        所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 

    text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串
    使用text结果又有乱码的话,需要设置编码方式
    r1.encoding="gbk"
    或者r1.encoding=r1.apparent_encoding

"""
# 例1:查看响应内容
"""
import requests
url = 'https://api.github.com/events'
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get(url,params = payload)
print(r.url) # url/get?key1=value&key2=value2&key2=value3
print(r.status_code,r.encoding,r.apparent_encoding,r.cookies.get_dict())
print(r.text)
print(r.content)
print(r.json())
"""
# 例2：原始响应内容
"""

import requests
url = 'https://api.github.com/events'
r = requests.get(url,stream=True)
#print(r.raw.read(10))
将文本流保存到文件
with open('log.txt', 'wb') as fd:
    for chunk in r.iter_content():
        fd.write(chunk)

"""