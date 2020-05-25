# -*- coding: utf-8 -*-
'''
### 小说爬取
import os
import re

from lxml import etree

import requests
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

def get_infos(url):
	# if not os.path.exists('F:/python代码\爬虫/fiction/Ch_text'):
	# 	os.mkdir('F:/python代码\爬虫/fiction/Ch_text')
	with open('F:/python代码\爬虫/fiction/Ch_text.txt','w',encoding='utf-8') as f:
		response=requests.get(url=url,headers=headers)
		html=response.content.decode('gbk')
		titles_lists = etree.HTML(html)
		text_lists=titles_lists.xpath('//td[@width="84%"]//p/font/text()')
		#print(text_lists)
		for t in text_lists:
			t=t.strip()
			t=t.replace(r'\r\n','')
			f.write(t)
	f.close()
## 报错：UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 189

def main():
	# url='http://en.eywedu.net/HXSZ/index.htm'
	# response=requests.get(url=url,headers=headers)
	# html=response.content.decode('gbk')
	# titles_lists=etree.HTML(html)
	# titles=titles_lists.xpath('//ul/p/text()')[0].strip().split(' ')[0]
	# chapters=titles_lists.xpath('//ul//li/a/text()')
	# chapter_lists=[str(chapter).replace('1','').strip() for chapter in chapters]
	# chapter_lists=''.join(chapter_lists).replace(' ','')
	#print(English_chapter)
	Ch_text=[]
	En_text=[]
	j=2
	for i in range(35):
		if i<10:
			url='http://en.eywedu.net/HXSZ/421c0179zw_000'+str(i+j)+'.htm'
			Chinese_detail_infos=get_infos(url)
			Ch_text.append(Chinese_detail_infos)
			
		else:
			url='http://en.eywedu.net/HXSZ/421c0179zw_00'+str(i)+'.htm'
			Chinese_detail_infos = get_infos(url)
			Ch_text.append(Chinese_detail_infos)
	
	
	# for i in range(18):
	# 	if i<4:
	# 		url='http://en.eywedu.net/HXSZ/421c0179zw_000'+str((i+1)*2)+'.htm'
	# 		English_detail_infos=get_infos(url)
	# 		En_text.append(English_detail_infos)
	#
	# 	else:
	# 		url='http://en.eywedu.net/HXSZ/421c0179zw_00'+str((i+1)*2)+'.htm'
	# 		English_detail_infos = get_infos(url)
	# 		En_text.append(English_detail_infos)
	# 		datas=parse_detail(English_detail_infos)
	
if __name__ == '__main__':
	main()
'''

### 电影票房数据爬取并保存到本地
from lxml import etree

import requests

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

def parse_url():
	pass


def main():
	m={}
	url = 'http://58921.com/alltime'
	response=requests.get(url=url,headers=headers)
	html=response.content.decode('utf-8')
	infos=etree.HTML(html)
	infos=infos.xpath('//div[@id="content"]')[0]
	title=infos.xpath('.//div/h3/text()')
	names=infos.xpath('.//tr/th/text()')
	details=infos.xpath('.//tbody')[0]
	movies=details.xpath('./tr//td[3]/a/text()')
	print(movies)
	


if __name__ == '__main__':
	main()