# -*- coding: utf-8 -*-
## 多线程队列
# import threading
# Value=0
# glock=threading.Lock()
# def add_value():  # 修改了全局变量的地方要加锁，其他地方不需要
# 	global Value  # 调用全局变量
# 	glock.acquire() # 加锁
# 	for x in range(10000000):
# 		Value+=1
# 	glock.release() # 解锁
# 	print('value: %d'%Value)
#
# def main():
# 	for x in range(2):
# 		t=threading.Thread(target=add_value())
# 		t.start()
# if __name__ == '__main__':
# 	main()
 
####  --------------多线程爬取斗图啦-----------------

## queue:安全队列创建
# from queue import Queue
#
# q=Queue(5) # 创建 5 个队列，相当于5个人一起行动，效率高
# q.put(1) # 加入一个数字 1
# q.put(3) # 加入一个数字 3
# print(q.qsize()) # 返回数字共有 2 个
# print(q.full()) # 当队列数等于加入的数字个数时即满，此时未满，返回布尔值
# for i in range(5):
# 	q.put(i)
# for i in range(5):
# 	print(q.get())
import time
from queue import Queue
import os
import re
from lxml import etree
import requests
from urllib import request
import threading

class Procuder(threading.Thread):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
	}
	def __init__(self,page_queue,img_queue,*args,**kwargs):
		super(Procuder,self).__init__(*args,**kwargs)
		self.page_queue=page_queue
		self.img_queue=img_queue
		
	def run(self):
		while True:
			if self.page_queue.empty():
				break
			url=self.page_queue.get()
			self.get_url(url)

	def get_url(self,url):
		reponse = requests.get(url=url, headers=self.headers)
		html = reponse.text
		img_urls = etree.HTML(html)
		## 去掉 class 是 gif 属性的一部分标签 img[@class!="gif"]，留下有数据的标签
		infos = img_urls.xpath('//ul[@class="list-group"]//a/img[@class!="gif"]')
		for imgs in infos:
			img = imgs.get('data-original')
			alt = imgs.get('alt')
			alt = re.sub(r'[\?？\.!]', '', alt)
			a = os.path.splitext(img)[1]  ## 分割文件与后缀名
			file = alt + a  # 拼出文件名
			print(file)
			self.img_queue.put((img,file)) # 返回元组

class Consumer(threading.Thread):
	def __init__(self,page_queue,img_queue,*args,**kwargs):
		super(Consumer,self).__init__(*args,**kwargs)
		self.page_queue=page_queue
		self.img_queue=img_queue
	
	def run(self):
		i=1
		while True:
			imgs,file=self.img_queue.get()
			request.urlretrieve(imgs,'F:/python代码/爬虫/doutuba/'+file)
			print('=== 下载完成%d张==='%i)
			if self.img_queue.empty():
				break
			i+=1
def main():
	page_queue=Queue(100)
	img_queue=Queue(500)
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	t=time.time()
	for x in range(start_page, end_page + 1):
		url = 'http://www.doutula.com/photo/list/?page='+str(x)
		page_queue.put(url)
		
	for x in range(10):
		ta=Procuder(page_queue,img_queue)
	
		ta.start()
	for x in range(10):
		tb=Consumer(page_queue,img_queue)
		tb.start()
		tb.join()
	print(time.time()-t)
if __name__ == '__main__':
	main()