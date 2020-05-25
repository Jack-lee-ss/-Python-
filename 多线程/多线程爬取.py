# -*- coding: utf-8 -*-
# import os
# import threading
# import time
# from queue import Queue
#
# def sail(q):
# 	while True:
# 		if q.empty():
# 			break
# 		print('----线程%s售出票：%d----'%(threading.current_thread().getName(),q.get()))
# 		time.sleep(1)
#
# def main():
# 	q=Queue(1000)
# 	for i in range(1000):
# 		q.put(i)
#
# 	threads=[]
#
# 	for i in range(100):
# 		t=threading.Thread(target=sail,args=(q,))
# 		t.start()
# 		threads.append(t)
# 	for t in threads:
# 		t.join()
# 	print('子线程任务结束，当前线程是： %s'%threading.current_thread().getName())
#
#
# if __name__== '__main__':
# 	main()

##### 英雄联盟英雄图片爬取
# import os
# import re
# from queue import Queue
# from urllib import request
# import requests
# from lxml import etree
# import json
# headers={
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
# }
# def parse_url(url,x):
# 	hero={}
# 	response=requests.get(url=url,headers=headers)
# 	data = response.text
# 	data=json.loads(data)
# 	skins=data['skins']
# 	j=1
# 	for i in range(len(skins)):
# 		if data['skins'][i]['chromas']==str(0):
# 			name=data['skins'][i]['name']
# 			mainImage=data['skins'][i]['mainImg']
# 			hero['name']=name
# 			hero['img']=mainImage
# 			heroes_imgs=download_imgs(hero,x,j)
# 			j+=1
# 	x+=1
# def download_imgs(infos,x,j):
#
# 	request.urlretrieve(infos['img'],'F:/python代码/爬虫/heors/'+infos['name']+'.jpg')
# 	print('==== 保存第%d个英雄第%d张图片==='%(x,j))
#
# def main():
# 	url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# 	response=requests.get(url=url,headers=headers)
# 	result=response.text
# 	data=json.loads(result)
# 	urls=data['hero'][0]['selectAudio']
# 	x=1
# 	base_urls = re.match(r'(.*img).*?',urls).group(0) + '/js/hero/'
# 	for i in range(len(data['hero'])):
# 		base_url=base_urls+str(i+1)+'.js'
# 		parse_url(base_url,x)
# 		x+=1
#
# if __name__== '__main__':
# 	main()


###### 多线程
