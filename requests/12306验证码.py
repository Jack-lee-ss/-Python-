# -*- coding: utf-8 -*-
## url 解码后不需要进行 requests 请求了。
'''
1，抓包。得到数据，查看验证码所在链接的响应数据

2，分析。Request URL: data:image/jpg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wB.....
   该网站验证码图片是通过 base64 加密生成。
   
3，获取验证码加密包，https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1586413079728&callback=jQuery191036803336134949105_1586412707126&_=1586412707129 由于login_site=E&module=login&rand=sjrand&1586413079728&callback=jQuery191036803336134949105_1586412707126&_=1586412707129 都是固定时间的数据，可以去掉（具体情况可以试一试，将链接放置浏览器中观察是否出现变动验证码图片即可）

4，得到 验证码包：https://kyfw.12306.cn/passport/captcha/captcha-image64  注意：该 image64 是对验证码的base64加密，所以去掉 64 。最终：https://kyfw.12306.cn/passport/captcha/captcha-image

5，构造登录包数据，模拟登录
'''
import requests

def get_point(indexs):
	point_map = {
		'1': '42,42',
		'2': '113,51',
		'3': '180,50',
		'4': '253,53',
		'5': '40,120',
		'6': '107,123',
		'7': '175,125',
		'8': '250,120'
	}
	indexlist=indexs.split(',')
	temp=[]
	for index in indexlist:
		temp.append(point_map[index])
	print(temp)
	return temp

def main():
	url='https://kyfw.12306.cn/passport/captcha/captcha-image' ## 图片链接，不需要requests请求了。直接反应的是图片。
	req=requests.session()
	result=req.get(url).content  ## 二进制内容
	
	with open('code_imge.png','wb')as f:  ## 保存验证码图片
		f.write(result)
		
	## 由于验证码图片是 4×2 排列的。一层4张图片，可以固定8张图片的坐标,用序号指定8张图片。
	
	code=get_point(input('请输入图片序号(1-8号): '))
	code_postion=','.join(code)
	print(code_postion)
	## 请求验证码校验包
	# url='https://kyfw.12306.cn/passport/captcha/captcha-check'
	#
	# data={
	# 	'answer':code_postion,
	# 	'rand': 'sjrand',
	# 	'login_site': 'E',
	# }
	# result=req.get(url=url,params=data)
	# #print(result.text)
	# print('=============')
	
	
	
	
	####### 模拟登录未成功 ###########
	url_login='https://kyfw.12306.cn/passport/web/login'
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '65',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		#'Cookie': '_passport_ct=e8b17f158a834424a5e26b8639a491bat1377; _passport_session=3ee92bde5f9b4cb8bc0a5dbd5acb8e095454; RAIL_EXPIRATION=1586676548461; RAIL_DEVICEID=JNEtl_uImaZRsGJq9ArbnfLKUoGGNv06QaA_jG-6e3OJV4T4zIhTc29FU5r9vAHL22kwKJz5r_bszCVY-nk8SqMbDgvxHeGmVlgy-cn0DNwoqJgElb-paSwgiTOZX-pzV9AfXC2bKFlIkRGv4H5IyuIIypsUyHID; BIGipServerpool_passport=401408522.50215.0000; route=495c805987d0f5c8c84b14f60212447d; BIGipServerpassport=854065418.50215.0000; BIGipServerportal=3067347210.17183.0000; BIGipServerotn=3705078026.64545.0000',
		'Host': 'kyfw.12306.cn',
		'Origin': 'https://kyfw.12306.cn',
		'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
		
	}

	data={
		'username': '17859737272',
		'password': '22222222',
		'appid': 'otn',
		'answer':code_postion
	}
	
	res=requests.session()
	resp=res.post(url=url_login,params=data)
	print(resp.content.decode('utf-8'))
	
	
	

if __name__ == '__main__':
	main()