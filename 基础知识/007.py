'''
### xpath
## 语法：① /和//的区别：前者只是获取直接子节点，后者获取子孙节点，一般//用的多，② 有时候一个属性中包含多个值时，可以使用'contains'函数，//div[contains(@class,'job_detail')],③ 谓词下标从1开始，而不是从0开始。

# 豆瓣电影爬取
import requests
from lxml import etree
url='https://movie.douban.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
response=requests.get(url=url,headers=headers)
#print(response.text) ## 解码过的数据
#print(response.content.decode('utf-8')) 效果相同
text=response.text

## 解析数据
# etree.HTML():构造了一个XPath解析对象并对HTML文本进行自动修正。
# etree.tostring()：输出修正后的结果，类型是bytes
html=etree.HTML(text)
## 输出是列表，必须选择下标，数组型
div_s=html.xpath('//div[@class="screening-bd"]')[0]
lis=div_s.xpath('./ul[@class="ui-slide-content"]')[0]
# print(lis)
# print(etree.tostring(lis,encoding='utf-8').decode('utf-8'))
movies=[]
for li in lis:
	title=li.xpath('./@data-title')
	img=li.xpath('.//img/@src')
	year = li.xpath('./@data-release')
	actors=li.xpath('./@data-actors')
	region=li.xpath('./@data-region')
	duration=li.xpath('./@data-duration')
	rate=li.xpath('./@data-rate')
	star=li.xpath('./@data-star')
	movie = {
			'title':title,
			'img':img,
			'year':year,
			'actors':actors,
			'region':region,
			'duration':duration,
			'rate':rate,
			'star':star

		}
	movies.append(movie)
print(movies)

'''


#========================================

'''
# 豆瓣热门电影爬取
import  requests
from lxml import etree
url='https://movie.douban.com/subject/30327842/?tag=%E7%83%AD%E9%97%A8&from=gaia'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
resp=requests.get(url=url,headers=headers)
response=resp.text
html=etree.HTML(response)
# print(html)
#print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
divs=html.xpath('//div[@id="content"]')[0]

# print(etree.tostring(divs,encoding='utf-8').decode('utf-8'))
title1=divs.xpath('.//h1/span[1]/text()')[0].strip()
title2=divs.xpath('.//h1/span[2]/text()')[0].strip()
title=title1+title2
img=html.xpath('.//div[@id="mainpic"]//img/@src')
info=html.xpath('//div[@id="info"]')[0]
director=info.xpath('.//span[@class="attrs"]/a/text()')[0]
screenwriter1=info.xpath('.//span[@class="attrs"]/a/text()')[1]
screenwriter2=info.xpath('.//span[@class="attrs"]/a/text()')[2]
#print(screenwriter1+","+screenwriter2)
screenwriter=screenwriter2+screenwriter1
actors=info.xpath('.//span[@class="actor"]')
for actor in actors:
	name=actor.xpath('.//span[@class="attrs"]//a/text()')
	#print(name)
type=info.xpath('.//span[@property="v:genre"]/text()')
region=info.xpath('.//br')
a_s=info.xpath('.//span[@class="pl"]')
#print(a_s)
# c=info.xpath('.//span[@class="pl"]')
# print(c[0])
for a in a_s:
	i=a.xpath('./text()')
	#print(i)
	
titles=info.xpath('.//span[@class="pl"]')[7]
#print(titles)

d=html.xpath('//div[@id="link-report"]/span/text()')

print(d)
'''

'''
# 80s热门电影爬取
import  requests
from lxml import etree

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

def get_url():
	url='http://www.y80s.com/movie/list'
	resp=requests.get(url=url,headers=headers)
	response=resp.text
	#print(response)
	html=etree.HTML(response)
	uls=html.xpath('//ul[@class="me1 clearfix"]')[0]
	li=uls.xpath('./li')
	for url_s in li :
		urls=url_s.xpath('./a/@href')[0]
		url= 'http://www.y80s.com'+ urls
		parse_detail(url)
def parse_detail(url):
	resp=requests.get(url,headers=headers)
	respose=resp.text
	html=etree.HTML(respose)
	divs=html.xpath('//div[@id="body"]')[0]
	imgs=divs.xpath('.//div[@class="img"]/img/@src')[0]
	img_s='http:'+imgs
	title=divs.xpath('.//div[@class="img"]/img/@title')[0]
	info=divs.xpath('.//div[@class="info"]')[0]
	
	actor1=info.xpath('.//div[@class="clearfix"]/span[1]//a/text()')
	actor2=info.xpath('.//div[@class="clearfix"]/span[2]//a/text()')
	#print(actor1+actor2)
	
	
	
	
	
	
	
	# type=info.xpath('.//span[2]/a/text()')[0]
	# if type.startswitch('又名'):
	# 	type=info.xpath('.//span[3]/a/text()')
	# 	print(type)
	#
	

	


if __name__ == '__main__':
	get_url()
	
	
	


# print(uls)
# print(etree.tostring(uls,encoding='utf-8').decode('utf-8'))

'''


# BT热门电影爬取

import  requests
from lxml import etree


header={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
	}
	
	
def get_url():
	url='http://www.1btjia.com/forum-index-fid-1.htm'
	resp=requests.get(url=url,headers=header)
	html=etree.HTML(resp.text)
	print(html)
	tables=html.xpath('//div[@class="div"]')[0]
	print(tables)
	# 提取后几个相同标签
	tablelist=tables.xpath('.//table[position()>5]')
#
# 	for urls in tablelist:
# 		#print(etree.tostring(urls, encoding='utf-8').decode('utf-8'))
# 		url=urls.xpath('.//a/@href')[0]
# 		#print(url)
# 		parse_detail_url(url)
#
# #解析每一个详情页
# def parse_detail_url(url):
# 	response=requests.get(url=url,headers=header)
# 	html=etree.HTML(response.text)
# 	movies=[]
# 	movie_info={}
# 	imgs1=html.xpath('//div[@class="bg1 border post"]//div/img/@src')
# 	imgs2=html.xpath('//div[@class="bg1 border post"]//p/img/@src')
# 	imgs=imgs1+imgs2
#
# 	titlelists=html.xpath('//div[@class="bg1 border post"]//h2/text()')
# 	for titlelist in titlelists:
# 		titles=titlelist.replace('\t','').strip()
#
# 	infos1=html.xpath('//div[@class="bg1 border post"]//div//p/text()')
# 	for infos in infos1:
# 		infos=''.join(infos.replace('\n',''))
# 		#print(infos)
# 	infos2=html.xpath('//div[@class="bg1 border post"]//div//span/text()')
# 	#movie_info = {}
# 	for info in infos2:
# 		if info.startswith('◎译　　名'):
# 			movie_info['name'] = info.replace("◎译　　名", "").strip()
# 			#print(movie_info)
# 		elif info.startswith('◎片　　名'):
# 			movie_info['title'] = info.replace("◎片　　名", "").strip()
# 		elif info.startswith('◎年　　代'):
# 			movie_info['year'] = info.replace("◎年　　代", "").strip()
# 		elif info.startswith('◎国　　家　'):
# 			movie_info['country'] = info.replace("◎国　　家　", "").strip()
# 		elif info.startswith('◎类　　别'):
# 			movie_info['type'] = info.replace("◎类　　别", "").strip()
# 		elif info.startswith('◎语　　言'):
# 			movie_info['language'] = info.replace("◎语　　言", "").strip()
# 		elif info.startswith('◎字　　幕'):
# 			movie_info['profits'] = info.replace("◎字　　幕", "").strip()
# 		elif info.startswith('◎片　　长'):
# 			movie_info['durtion'] = info.replace("◎片　　长", "").strip()
# 		elif info.startswith('◎导　　演'):
# 			movie_info['director'] = info.replace("◎导　　演", "").strip()
# 		elif info.startswith('◎IMDB评分'):
# 			movie_info['IMDB评分'] = info.replace("◎IMDB评分", "").strip()
# 		elif info.startswith('◎文件格式'):
# 			movie_info['文件格式'] = info.replace("◎文件格式", "").strip()
# 			a=''.join(movie_info)
# 			print(a+infos)
# 			#print(list(movie_info))
#
#
# 	# infos=infos1+infos2
# 	# i=''.join(infos).replace('\n',"")
# 	# #print(i)
# 	# information=list(i.split('1'))
# 	#print(information)
# 	# for info in infos:
# 	# 	information=info.replace('\n','').replace('1','')
# 		#print(information)
#
# 	downloads=html.xpath('//div[@class="attachlist"]//tr//a/text()')
# 	info={
# 		'imgs':imgs,
# 		'titles':titles,
# 		'information':movie_info,
# 		'downloads':downloads
# 	}
# 	movies.append(info)
# 	# print(movies)
# 	# print('=====' * 10)
# if __name__ == '__main__':
# 	get_url()




### =================== BT电影爬取==========================
# from lxml import etree
#
# import  requests
#
# header={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# 	}
#
# def parse_detail_urls(url):
# 	response = requests.get(url=url, headers=header)
# 	html = etree.HTML(response.text)
# 	movie = {}
# 	imgs1 = html.xpath('//div[@class="bg1 border post"]//div/img/@src')
# 	imgs2 = html.xpath('//div[@class="bg1 border post"]//p/img/@src')
# 	imgs=imgs1+imgs2
# 	movie['imgs']=imgs
# 	titlelists = html.xpath('//div[@class="bg1 border post"]//h2/text()')
# 	for titlelist in titlelists:
# 		titles = titlelist.replace('\t', '').strip()
# 		movie['titles']=titles
#
# 	infos = html.xpath('//div[@class="bg1 border post"]//div//p/text()')
# 	for info in infos:
# 		info_handle = info.replace('\n', '')
# 		movie['info_handle']=info_handle
#
# 	downloads = html.xpath('//div[@class="attachlist"]//tr//a/text()')
# 	movie['downloads']=downloads
# 	movie={
# 		'imgs':imgs,
# 		'titles':titles,
# 		'info_handle':info_handle,
# 		'downloads':downloads
# 	}
# 	print(movie)
#
# def spider():
# 	url='http://www.1btjia.com/forum-index-fid-1.htm'
# 	resp = requests.get(url=url, headers=header)
# 	html = etree.HTML(resp.text)
#
# 	tables = html.xpath('//div[@class="div"]')[0]
# 	# 提取后几个相同标签
# 	tablelist = tables.xpath('.//table[position()>5]')
#
# 	for urls in tablelist:
# 		# print(etree.tostring(urls, encoding='utf-8').decode('utf-8'))
# 		urls= urls.xpath('.//a/@href')
# 	# 解析网页
# 		infomations=parse_detail_urls(urls)
# 	movies=[]
# 	movies.append(infomations)
# 	#print(movies)
#
# if __name__ == '__main__':
# 	spider()
	
	
	