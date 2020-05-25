####  ========================  爬虫 ==========================
## urllib 库 ：基本的网络请求库
## request 模块

# urlopen 函数
# encoding: utf-8
from urllib import request
resp=request.urlopen('https://www.baidu.com') # 鼠标点到函数，ctrl+1 进入函数，出现蓝色底线。
print(resp.read())
# 读取第一行readline()，，读取多行readlines()
# print(resp.readline())

# urlretrieve函数 ：保存数据，下载数据
#request.urlretrieve('http://dmimg.5054399.com/allimg/pkm/pk/22.jpg','皮卡球.jpg')


## parse 模块

# urlencode 函数：对字典数据进行编码，类似url地址格式，name=%E5%BC%A0%E4%B8%89&age=18%E5%B2%81&adress=%E5%8C%97%E4%BA%AC.   该函数在 parse 模块下
# from urllib import parse
# # a={'name':'张三','age':'18岁','adress':'北京'}
# # result=parse.urlencode(a)
# # print(result)
#
# ## 构造url （一般情况，请求的url中不可以带中文，不然无法通过ASCII码解析，需要先将中文部分编码在发送请求）
#
# # urlencode函数：编码函数
# # a=request.urlopen('https://www.baidu.com/s?wd=梅西') 会报错
# b={'wd':'梅西'}
# a=parse.urlencode(b)
# #print(a)
# url='https://www.baidu.com/s?'+a
# print('编码后')
# print(url)
#
# ## parse_qs 函数：解码函数，将ASCII解码成中文等字符串,返回值是列表
# c=parse.parse_qs(url)
# print('解码后')
# print(c)
#
# ### urlparse函数，urlsplit函数 ：用法基本一致，解析函数，将url解析成部分片段,只是前者多了一个 params 属性。
# from urllib import parse
# url='http://www.baidu.com/s?wd=python&user=abc&size=gkb'
# parse.urlparse(url)
# print(parse.urlparse(url))
# print(parse.urlsplit(url))

### 在回到 request 模块中，
# request.Request类,设置请求头。
from urllib import request
from urllib import parse
## 拉钩网
# url='https://www.lagou.com/beijing-zhaopin/?utm_source=m_cf_cpt_baidu_pc1'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
# ## 创建对象,返回值是内存信息。
# req=request.Request(url=url,headers=header)
# ## 打开网页，注意read()
# result=request.urlopen(req)
# print(result.read())

# url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&  needAddtionalResult=false&isSchoolJob=0'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36','Referer': 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=p','Accept': 'application/json, text/javascript, */*; q=0.01','method':'post'}
# data={'first': 'true','pn':'1','kd': 'python'}
#
# #'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=p'
# req=request.Request(url=url,data=parse.urlencode(data).encode('utf-8'),headers=header)
# respose=request.urlopen(req)
# print(respose.read().decode('utf-8'))  ###  无法爬取

#==========================

###  requests库
## get请求方式：
# import requests
# response=requests.get('https://www.baidu.com')
# ## 获取数据类型是字节型
# print(type(response.content))
# print('-----------------')
# ## 部分数据加密，无法识别
# print(response.content)
# print('-----------------')
# ## 含有乱码
# print(response.text)
# print('-----------------')
# ## 解码后可以识别的类型，推荐使用
# print(response.content.decode('utf-8'))
# print('-----------------')
# ### 获取地址与编码方式
# print(response.url)
# print(response.encoding)

## post请求方式  拉勾网爬虫 requests.post()

## 处理cookie信息
import requests
url='https://www.baidu.com/'
response=requests.get(url)
## 以字典形式返回cookie信息
print(response.cookies.get_dict())















