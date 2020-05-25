# -*- coding: utf-8 -*-
import json

import requests

def main():
	url='https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1A55E871C7676A&cp=5E7CD6F7162ADE1&_signature=EyoQwAAgEBDVfalNjpnUmhMrUdAAE1bP0kjz.8d2xIzkEjeiOyLOd1X8lb9kzZYTRCSrbwzy1pgq7QRl3dBV1Ai4e1--q097DdDEyK1PlVsm-2y1K2dr4vIDdKBlmNscd2b'
	
	headers={
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
	
	response=requests.get(url=url,headers=headers)
	result=response.text
	result=json.loads(result)
	datas=result['data']
	
	new={}
	news=[]
	for data in datas:
		new['标题']=data['title']
		new['简要']=data['abstract']
		new['来源']=data['source']
		new['图片']=data['image_url']
		news.append(new)
		print(new)


if __name__ == '__main__':
	main()