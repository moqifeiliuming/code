# 网络爬虫的基本工作流程如下：
# 1、获取初始的URL，该URL地址是用户自己指定的初始爬取的网页
# 2、爬取对应的URL地址的网页时，获取新的URL地址
# 3、将新的URL地址放入URL队列中
# 4、从URL队列中读取新的URL，然后根据新的URL爬取网页，同时从新的网页中获取新的URL地址，重复上述的爬取过程
# 5、设置停止条件，如果没有设置停止条件，爬虫会一直爬取下去，直到无法获取新的URL地址为止。设置了停止条件，爬虫将会在满足停止条件时停止爬取
# Python中实现HTTP网络请求常见的三种方式：urllib、urllib3、requests

# import urllib.request
# # 打开指定需要爬取的网页
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()  # 读取网页代码
# print(html)             # 打印读取内容

import urllib.request
import urllib.parse

# 将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
html = response.read()    # 读取网页内容
print(html)               # 打印读取内容

import urllib3
# 创建PoolManager对象，用于处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 对需要爬取的网页发送请求
response = http.request('GET','https://www.baidu.com')
print(response.data)
# 对需要爬取的网页发送请求
response = http.request('POST','http://httpbin.org/post',fields={'word':'hello'})
print(response.data)

# requests是python中实现HTTP请求的一种方式，requests是第三方模块，该模块在实现HTTP请求时要比urllib模块简化很多，操作更加人性化
import requests
response = requests.get('http://www.baidu.com')
print("打印状态码：",response.status_code)        # 打印状态码
print("打印URL：",response.url)                  # 打印请求url
print("打印头部信息：",response.headers)           # 打印头部信息
print("打印cookie信息：",response.cookies)        # 打印cookie信息
print("以文本形式打印：",response.text)            # 以文本形式打印网页源码
print("以字节流形式打印：",response.content)       # 以字节流形式打印网页源码

import requests
payload = {'key1':'value1','key2':'value2'}   # 传递的参数
# 对需要爬取的网页发送请求
response = requests.get("http://httpbin.org/get",params=payload)
print('\n',response.content)                  # 以字节流形式打印网页源码

import requests
# 循环发送请求50次
for a in range(0,20):
    try:
        #设置超时为0.5秒
        response = requests.get('https://www.baidu.com',timeout=0.5)
        print(response.status_code)
    except Exception as e:
        print('异常'+str(e))

# import requests
# # 导入requests.exceptions模块中的3中异常类
# from requests.exceptions import ReadTimeout,HTTPError,RequestException
# # 循环发送请求50次
# for a in range(0,10):
#     try:
#         # 设置超时为0.5秒
#         response = requests.get('http://www.badidu.com',timeout=0.5)
#         print(response.status_code)         # 打印状态码
#     except ReadTimeout:                     # 超时异常
#         print('timeout')
#     except HTTPError:                       # HTTP异常
#         print('httperror')
#     except RequestException:
#         print('reqerror')                   # 请求异常

# import requests
# proxy = {'http':'122.114.31.177:808',
#          'https':'122,114,31,177:8080'} #设置代理ip与对应的端口号
# # 对需要爬取的网页发送请求
# response = requests.get('http://www.mingrisoft.com/',proxies=proxy)
# print(response.content)    # 以字节流形式打印网页源码

# Beautiful Soup 是一个用于从HTML和XML文件中提取数据的Python库，其提供一些简单的函数来处理导航、搜索、修改分析树等功能。
# Beautiful Soup 模块中的查找提取功能非常强大，而且非常便捷，通常可以节省程序员大量的工作时间

from bs4 import BeautifulSoup    # 导入Beautiful Soup库
# 创建模拟HTML代码的字符串
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2>Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建一个Beautiful Soup对象，获取页面正文
soup = BeautifulSoup(html_doc,features="1mxl")
print(soup)

# 创建Beautiful Soup对象打开需要解析的html文件
soup = BeautifulSoup(open('index.html'),'1xml')
print(soup.prettify())    # 打印格式化后的代码

# Crawley的官网地址为：http://project.crawley-cloud.com
# PySpider源码地址为：http://github.com/binux/pyspider/releases
# 开发文档地址为：http://docs.pyspider.org/
# QT工具下载：http://www.qt.io/download

# CGI(Common Gateway Interface)，即通用网关接口，是一段程序，运行在服务器上。Web服务器将请求发送给CGI应用程序，再将CGI应用程序动态生成的HTML页面发送返回客户端。
# CGI在Web服务器和应用之间充当了交互作用，这样才能够处理用户数据，生成并返回最终的动态HTML页面。
# CGI有明显的局限性，CGI进程针对每个请求进行创建，用完就抛弃。如果应用程序接收数千个请求，就会创建大量的语言解释器进程，会导致服务器停机。
# FastCGI使用进程/线程池来处理一连串的请求，这些进程/线程由FastCGI服务器管理，而不是Web服务器，FastCGI致力于减少网页服务器与CGI程序之间交互的开销，从而使服务器可以同时处理更多的网页请求。
# FastCGI的标准下写异步的Web服务器不是很方便，因此WSGI(Web Server Gateway Interface)，即服务器网关接口，是Web服务器和Web应用程序或者框架之间的一种简单而通用的接口。从层级上来讲要比CGI/FastCGI高级。
# WSGI中存在两种角色：接受请求的Server(服务器)和处理请求的Application(应用)，它们底层是通过FastCGI沟通的。当Server收到一个请求后，可以通过Socket把环境变量和一个Callback回调函数传给后端Application，
# Application在完成页面组装后通过Callback把内容返回给Server，最后Server再将响应返回给Client。

# Python常用的Web框架
# Flask：是一款轻量级Web应用框架，基于Werkzeug实现的WSGI和Jinja2模板引擎。通过扩展机制来增加其他功能
# Django：市场上提供了非常齐备的官方文档以及一站式解决方案，包括缓存、ORM/管理后台、验证、表单处理等，使开发复杂的数据库驱动的网站变得更加简单。但是其系统耦合度太高，替换内置的功能往往会占用一些时间
# Bottle：一款轻量级的Web框架，只有一个文件，只使用了Python标准库，自带了路径映射、模板、简单的数据库访问等Web框架组件，不需要额外依赖其他第三方库，更符合微框架的定义，语法简单，部署也很方便
# Tornado：全称(Tornado Web Server)，其实非阻塞式服务器，速度相当快，每秒钟可以处理数以千计的连接，对于长轮询、WebSocket等Web服务来说，是一个理想的Web框架

