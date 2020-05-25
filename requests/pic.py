# -*- coding: utf-8 -*-
import os
import requests
from lxml import etree
from urllib import request

headers = {
	'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36'
}

def get_url_parse(result):
	html = etree.HTML(result)
	urls = html.xpath('//*[@id="tpl-img-content"]/li/a/@href')
	for url in urls:
		urlss = 'https://www.95ndy.com/' + url
		response = requests.get(url=urlss, headers=headers)
		result = response.content.decode('utf-8')
		html = etree.HTML(result)
		imgs = html.xpath('//div[@class="content"]//img[@class="videopic lazy"]')
		i=1
		for img in imgs:
			img1 = img.get('data-original')
			file='第'+str(i)+'张'+'.jpg'
			req = requests.session()
			result = req.get(img1).content
			with open('F:/python代码/爬虫/pic/'+file, "wb")as f:
				f.write(result)
			print('===== 第%d张===='%i)
			i+=1

def main():
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	
	for x in range(start_page, end_page + 1):
		# requests=requests.session()
		url = 'https://www.95ndy.com/tupian/list-卡通动漫' + str(-x) + '.html'
		response = requests.get(url=url, headers=headers)
		result = response.content.decode('utf-8')
		# print(result)
		# print('=========')
		get_url_parse(result)


if __name__ == '__main__':
	main()