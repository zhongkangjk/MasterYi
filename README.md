我的笔记
====
20190810
----
requests的一个爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
        
20190812
----
BeautifulSoup
标签树的下行遍历
.contents#将<tag>所有子节点存入列表
.children#子节点的迭代类型
.descenants#子孙节点的迭代类型
标签树的上行遍历
.parent#节点的父标签
.parents#节点先辈标签的迭代类型
标签树的平行遍历
.next_sibling#返回按照HTML文本顺序的下一个平行标签
.previous_sibling#返回按照HTML文本顺序的上一个平行标签
.next_siblings#迭代类型后续所有平行节点标签
.previous_sibling#迭代类型前续所有平行节点标签
bs4库的prettify()方法  加空格

20190821
----
正则表达式
字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
多数字母和数字前加一个反斜杠时会拥有不同的含义。
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

20190824
----
Scrapy
scrapy startproject python123demo
创建一个名为python123demo的工程
cd python123demo 进去
scrapy genspider demo python123.io
创建一个名为demo的爬虫以爬取python123.io
scrapy crawl demo
执行demo




Scrapy中的

Request对象表示一个HTTP请求
由Spider生成，由Downloader执行
Request的属性或方法
.url Request对应的请求URL地址
.method对应的请求方法，‘GET’‘POST’等
.headers字典风格的请求头
.body请求内容主题，字符串类型
.meta用户添加的扩展信息，在Scrapy内部模块间传递信息使用
.copy()复制该请求

Response对象表示一个HTTP响应
由Downloader生成，由Spider处理
Response的属性或方法
.url Response对应的URL地址
.status HTTP状态码，默认是200
.headers Response对应的头部信息
.body Response对应的内容信息，字符串类型
.flags 一组标记
.request 产生Response类型对应Request对象
.copy()复制该响应

Item对象表示一个从HTML页面中提取的信息内容
由Spider生成，由Item Pipeline处理
类似字典类型，可以按照字典类型操作

20190831
----
gedit /etc/apt/sources.list
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free 
apt-get update
apt-get upgrade
清华源更新kali

20190909
----
时间片流转
并行：真的多任务
并发：假的多任务
threading.Thread(target =).start  创建跑
threading.enumerate()  返回一个线程列表

20190911
----
锁 = threading.Lock()
锁.acquire()  #上锁   如果之前没上锁的话
锁.release()  #解锁

20190913
----
进程：资源分配的单位
线程：操作系统调度的单位
range():产生一个列表   python2瞬间爆炸   
xrange():一个生产列表的方法   占用资源小 什么时候用什么时候产
这也是迭代器的优点

20190917
----
xx:公有变量
_x:私有化属性或者方法，禁止导入，类对象和子类可以访问
__xx:避免和子类命名冲突，无法在外部直接访问
__xx__:用户名字空间的魔法对象或属性，__init__，不要自己发明
xx_:避免和关键词冲突

20190918
----
selenium 显性等待
WebDriverWait(driver,10).until(lambda the_driver:the_driver.find_element_by_xpath())
driver.find_element_by_xpath().click()


20190929
----
我使用了django1.8.2
django-admin startproject test1  #创建了一个test1项目
进入test1文件夹创建应用
python manage.py startapp 应用名
进settings.py INSTALLED_APPS #进行应用注册
python manage.py runserver 运行起来
数据库：在models.py创建一个模型类
python manage.py makemigrations #生成迁移文件
python manage.py migrate #执行迁移生成表（默认sqlite3）
#略学不下去


20191002
----
scrapy startproject mySpider创建项目
scrapy genspider itcast "itcast.cn" 创建一个爬虫
到项目文件夹 scrapy crawl itcast 启动这个爬虫
不让日志显示 去settings加LOG_LEVEL = "WARNING" 比""小的日志都不会显示出来"
response.xpath('//div[@class="tea_con"]//h3/text()').extract()
为了不加xpath只显示文字在后面加.extract()
只去第一个值.extract_first()
到settings开启ITEM_PIPELINES

20191007
----
#保存
dict_name = {1:{1:2,3:4},2:{3:4,4:5}}
f = open('temp.txt','w')
f.write(str(dict_name))
f.close()
 
#读取
f = open('temp.txt','r')
a = f.read()
dict_name = eval(a)
f.close()

在 scrapy 中，

scrapy.Request(url, headers=self.header, callback=self.parse_detail)
1
调试的时候，发现回调函数 parse_detail 没有被调用，这可能就是被过滤掉了，查看 scrapy 的输出日志 offsite/filtered 会显示过滤的数目。这个问题如何解决呢，查看手册发现(https://doc.scrapy.org/en/latest/faq.html?highlight=offsite%2Ffiltered)这个问题，这些日志信息都是由 scrapy 中的一个 middleware 抛出的，如果没有自定义，那么这个 middleware 就是默认的 Offsite Spider Middleware，它的目的就是过滤掉那些不在 allowed_domains 列表中的请求 requests。

再次查看手册中关于 OffsiteMiddleware 的部分(https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.offsite.OffsiteMiddleware) 
两种方法能够使 requests 不被过滤: 
1. 在 allowed_domains 中加入 url 
2. 在 scrapy.Request() 函数中将参数 dont_filter=True 设置为 True









