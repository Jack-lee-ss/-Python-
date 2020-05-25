# encoding='utf-8'

####  ----------- 斗图啦爬取 ---------------------
import os
import re
import time

from lxml import etree
import requests
from urllib import request

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}


def get_url(url, x):
	i = 1
	reponse = requests.get(url=url, headers=headers)
	html = reponse.text
	img_urls = etree.HTML(html)
	infos = img_urls.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
	for imgs in infos:
		img = imgs.get('data-original')
		#print(img)
		alt = imgs.get('alt')
		alt = re.sub(r'[\\?？\.!(N)\*0:]', '', alt)
		a = os.path.splitext(img)[1]  ## 分割文件与后缀名
		file = alt + a  # 拼出文件名
		#print(file)
		request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + file)  # 保存图片并且给图片起名
		print('===========保存第%s页第%s张============' % (x, i))
		i += 1

def main():
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	t1=time.time()
	for x in range(start_page, end_page + 1):
		url = 'http://www.doutula.com/photo/list/?page=' + str(x)
		#print(url)
		url_list = get_url(url, x)  # 获取 地址
	t2=time.time()
	print("总共用时{}秒".format((t2 - t1)))
	
if __name__ == '__main__':
	main()



###  美图录不同标签多页爬取

# import os
# import re
# from lxml import etree
# import requests
# from urllib import request
#
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
#
# def get_url(url, x):
# 	i = 1
# 	reponse = requests.get(url=url, headers=headers)
# 	html = reponse.content.decode('utf-8')
# 	img_urls = etree.HTML(html)
# 	infos = img_urls.xpath('//div[@class="boxs"]//img')
# 	for imgs in infos:
# 		img = imgs.get('src')
#
# 		alt = imgs.get('alt')
#
# 		#alt = re.sub(r'', '', alt)
# 		a = os.path.splitext(img)[1]  ## 分割文件与后缀名
# 		file = alt + a  # 拼出文件名
# 		try:
# 			request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + file)  # 保存图片并且给图片起名
# 			print('===========保存第%s页第%s张============' % (x, i))
# 			i += 1
# 		except FileNotFoundError:
# 			print('++++++ 缺少第%s张（%s）的图片 +++'%(i,file))
# 			i+=1
#
# def main():
# 	start_page = int(input('请输入大于1的起始页码：'))
# 	end_page = int(input('请输入不大于38的结束页码：'))
# 	for x in range(start_page, end_page + 1):
# 		url = 'https://www.meitulu.com/t/nvshen/'+ str(x)+'.html'
#
# 		url_list = get_url(url, x)  # 获取 地址
#
#
# if __name__ == '__main__':
# 	main()
#
#
#
# ###  发表情斗图爬取
# import os
# import re
# import time
#
# from lxml import etree
# import requests
# from urllib import request
#
# headers={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
#
# def get_url(url,x):
# 	i=1
# 	reponse=requests.get(url=url,headers=headers)
# 	html=reponse.text
# 	img_urls=etree.HTML(html)
# 	infos=img_urls.xpath('//div[@id="container"]//img')
# 	for imgs in infos:
# 		img=imgs.get('data-original')
# 		alt=imgs.get('alt')
# 		alt=re.sub(r'[\\?？\.!(N)\*0:]','',alt)
# 		a=os.path.splitext(img)[1]  ## 分割文件与后缀名
# 		file=alt+a  # 拼出文件名
# 		#print(file)
# 		request.urlretrieve(img,'F:/python代码/爬虫/doutuba/'+file) # 保存图片并且给图片起名
# 		print('===========保存第%s页第%s张============'%(x,i))
# 		i+=1
#
#
# def main():
# 	start_page=int(input('请输入起始页码：'))
# 	end_page=int(input('请输入结束页码：'))
# 	for x in range(start_page,end_page+1):
# 		url = 'https://www.fabiaoqing.com/biaoqing/lists/page/'+str(x)+'.html'
# 		#print(url)
# 		url_list=get_url(url,x)   # 获取 地址
#
# if __name__ == '__main__':
# 	main()
#
#
# # ##########  美图录女神标签下单人专属多页爬取
# import os
# import re
# from lxml import etree
# import requests
# from urllib import request
#
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
#
# ## 解析网页图片
# def get_url(url):
# 	reponse = requests.get(url=url, headers=headers)
# 	html = reponse.content.decode('utf-8')
# 	img_urls = etree.HTML(html)
# 	infos = img_urls.xpath('//ul[@class="img"]/li')
# 	for imgs in infos:
# 		url=imgs.xpath('./a/@href')[0]
# 		num=imgs.xpath('./p/text()')[0]
# 		num=re.search(r'\d+',num).group()
# 		# 调用获取专属图片函数
# 		data=parse_url(url, num)
#
# # 获取个人专属图片
# def parse_url(url,num):
# 	i=1
# 	# 构造个人专属总图片数与页码关系
# 	for x in range(int(int(num)/4)+1):
# 		if x==0:
# 			url_page=url
# 		else:
# 			url_page=re.sub(r'\.html','_'+str(x+1)+'.html',url)
#
# 		response=requests.get(url=url_page,headers=headers)
# 		html=response.content.decode('utf-8')
# 		infos_list=etree.HTML(html)
# 		infos=infos_list.xpath('//div[@class="content"]//img')
#
# 		for imgs in infos:
# 			img=imgs.get('src')
# 			alt=imgs.get('alt')
# 			a=os.path.splitext(img)[1]
# 			filename=alt+a
# 			try:
# 				request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + filename)  # 保存图片并且给图片起名
# 				print('===========保存%s高清图片============' % (alt))
# 				i += 1
# 			except FileNotFoundError:
# 				print('++++++ 缺少%s的图片 +++'%(alt))
# 				i+=1
#
# def main():
# 	start_page = int(input('请输入从1起始的页码：'))
# 	end_page = int(input('请输入不大于38的结束页码：'))
# 	for x in range(start_page, end_page+1):
# 		if x==1:
# 			url = 'https://www.meitulu.com/t/nvshen/'
# 			a= get_url(url)
# 		else:
# 			url = 'https://www.meitulu.com/t/nvshen/' + str(x) + '.html'
# 			a= get_url(url)  # 获取 地址
#
# if __name__ == '__main__':
# 	main()



