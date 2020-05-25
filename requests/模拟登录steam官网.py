# -*- coding: utf-8 -*-
import time
import requests
import execjs
def main():
	
	session=requests.session()
	ts=int(time.time()*1000)
	data={
		
		'donotcache': ts,
		'username':'111'
	}
	result=session.post('https://store.steampowered.com/login/getrsakey/',data=data).json()
	publickey_mod=result['publickey_mod']
	publickey_exp=result['publickey_exp']
	timestamp=result['timestamp']
	
	with open(r'F:\python代码\Python 基本操作\requests\steam.js','r',encoding='utf-8') as f:
		JSdata=f.read()
		print('=========')
	text=execjs.compile(JSdata).call('MyObj','1111',publickey_mod,publickey_exp)
	#print(text)
	
	
	headers={
		'Host': 'store.steampowered.com',
		'Origin': 'https://store.steampowered.com',
		'Referer': 'https://store.steampowered.com/login/?redir=&redir_ssl=1',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest'
	}
	
	data={
		'donotcache': ts,
		'password':text,
		'username': '111',
		'twofactorcode':'',
		'emailauth':'',
		'loginfriendlyname':'',
		'captchagid': '-1',
		'captcha_text':'',
		'emailsteamid':'',
		'rsatimestamp': timestamp,
		'remember_login': 'false'
	
	}
	result=session.post('https://store.steampowered.com/login/dologin/',data=data,headers=headers)
	print(result.text)
	
if __name__ == '__main__':
	main()