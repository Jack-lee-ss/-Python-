# -*- coding: utf-8 -*-
import requests
# url='https://www.baidu.com/'
# r=requests.get(url=url)
# #print(r.text)   ## 返回正文信息，源码，可能有乱码
# print(r.encoding) # 返回编码方式
# print(r.url) # 地址
# print(r.headers) # 请求头部
# print(r.cookies) # 缓存
# print(r.content) # 二进制文本
# print(r.status_code) # 状态码
# url='https://c.m87.pw/auth/login'
# data={
# 'email': 'lcq@163.com',
# 'passwd': '11111111',
# 'code':''
# }
# result=requests.post(url=url,data=data)
# print(result.status_code)
# print(result.encoding)
# print(result.text)
# print(result.text.encode('utf-8').decode('unicode_escape'))
#
# url='https://www.lagou.com/'
# headers={
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
# }
# # result=requests.get(url=url,headers=headers)
# print(result.text)

'''
#### 两种下载图片方法：
		一、流模式：
		url='https://pic.hmpicimage.com/katong/2020/04/12/AOYI5JAJFQIILA7C/001.jpg'
		headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
		#result=requests.get(url=url,headers=headers,stream=True)## 打开流模式，结束后需要关闭
		from contextlib import closing
		with closing(requests.get(url=url,headers=headers,stream=True)) as result: ## 关闭
			with open('./pict.png','wb')as f:
				for chunk in result.iter_content(128):
					f.write(chunk)
		print('=======')
		
		二、Session:
		url='https://pic.hmpicimage.com/katong/2020/04/12/AOYI5JAJFQIILA7C/001.jpg'
		headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
		session=requests.session()
		resp=session.get(url=url,headers=headers).content
		with open('./pict11.png','wb')as f:
			f.write(resp)
		print('=======')
'''

#### 钩子事件
url='https://www.243hm.com/index.html'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


def get_key_info(response,*args,**kwargs):
	print(response.headers['Content-Type'])


def main():
	requests.get(url=url,hooks=dict(response=get_key_info))

main()