# -*- coding: utf-8 -*-
import re

import requests
# def main():
# 	url='http://api.douguo.net/recipe/flatcatalogs HTTP/1.1'
# 	headers={
# 		'client': '4',
# 		'version': '6922.2',
# 		'device': 'MuMu',
# 		'sdk': '23,6.0.1',
# 		#'imei': '530000000098300',
# 		'channel': 'zhuzhan',
# 		'mac': '02:00:00:00:00:00',
# 		'resolution': '1024*576',
# 		'dpi': '1.2',
# 		'brand': 'Android',
# 		'scale': '1.2',
# 		'timezone': '28800',
# 		'language': 'zh',
# 		'cns': '0',
# 		'carrier': '%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A',
# 		'imsi': '460062092198883',
# 		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36',
# 		'reach': '1',
# 		'newbie': '1',
# 		'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
# 		'Accept-Encoding': 'gzip, deflate',
# 		'Connection': 'Keep-Alive',
# 		#'Cookie': 'duid=63669188',
# 		'Host': 'api.douguo.net',
# 		#'Content-Length': '68',
#
# 	}
#
# 	data={
# 		'client': '4',
# 		#'_session': '1585207071948530000000098300',
# 		#'v': '1585200819',
# 		#'order': '0',
# 		'_vs': '400',
# 	}
# 	response=requests.post(url=url,headers=headers,data=data)
# 	print(response)
#
#
# if __name__ == '__main__':
# 	main()
	

import json
# str = '{"params":{"id":222,"offset":0},"params1":["n. 钥匙;（打字机等的）键;关键，线索，秘诀;（音乐的）调","vt. 键入;锁上;调节…的音调;提供线索"]}'
# print(type(str))
#
# obj=re.search(r'"translation":(.*?])',str).group(1)
# print(obj)


# param = json.loads(str)
# print(type(param))
# print(param['params1'])

'''

我们保存的数据不能以字符串或者列表形式


'''
# liststr=[1,2,3,'adg']
# listdir={'city':'武汉','name':'黄冈'}
# list=json.dumps(liststr)
# dir=json.dumps(listdir,ensure_ascii=False) ## json.dumps()序列化是默认使用ASCII编码
# dir1=json.dumps(listdir)
# print(dir1)
# print(list)
# print(dir)
#
#
# ##  json.dump():保存数据到本地,将Python对象序列化写入文件中，针对文件操作
# with open('list.txt','w',encoding='utf-8') as f:
# 	json.dump(liststr, f, ensure_ascii=False) # 如果不加 ensure_ascii=False, gbk格式

## json.load():将文本数据导入到编辑器中，字符串格式转化为python类型
# f=open('list.txt',encoding='utf-8')
# list1=json.load(f)
# print(list1)
# f.close()


from urllib.request import urlretrieve
from urllib import request
import requests
import os
#with open('F:/python代码/Python 基本操作/requests/picts/1111.txt','w')as f:
	
# img1='https://mmtp1.com/maomao/katong/275/01.jpg'
# #f.write(img1)
#request.urlretrieve(https://mmtp1.com/maomao/katong/347/01.jpg,'皮卡球.jpg')
#print('===========')
#
# from urllib import request
# import urllib
# url = "https://mtl.gzhuibei.com/images/img/2876/1.jpg"
# data =requests.get(url)
# # f = open('F:/python代码/Python 基本操作/requests/picts/',"wb")
# # f.write(data)
# # f.close()
# print(data.status_code)
#
# with open('F:/python代码/Python 基本操作/requests/picts',"wb")as f:
# 	f.write(data.content)
# 	print('=========')

# url='http://manhua1032-61-174-50-98.cdndm5.com/38/37716/506471/1_3252.jpg?cid=506471&key=9717b7bfe737c73d206b6d0bc36328d8&uk='
# req=requests.session()
# result=req.get(url).content
# with open('1123.png',"wb")as f:
# 	f.write(result)
# print('=========')


# http://manhua1032-61-174-50-98.cdndm5.com/38/37716/506471/1_3252.jpg?cid=506471&key=9717b7bfe737c73d206b6d0bc36328d8&uk=


headers={
'Referer': 'http://www.dm5.com/m9835/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
url = "http://manhua1014-61-174-50-99.cdndm5.com/l/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B[%E7%AF%AE%E7%90%83%E9%A3%9E%E4%BA%BA]/%E6%A8%BD%E7%AF%AE%E9%AB%98%E6%89%8B1/slamdunk_01_021.jpg?cid=9835&key=0c6c9a083d66cba3d01b83c79998f9a9&uk="
#data =requests.get(url=url,headers=headers)
#result=requests.get(url=url,headers=headers,stream=True)## 打开流模式，结束后需要关闭
from contextlib import closing
with closing(requests.get(url=url,headers=headers,stream=True)) as result: ## 关闭
	with open('./pict.png','wb')as f:
		for chunk in result.iter_content(128):
			f.write(chunk)
print('=======')