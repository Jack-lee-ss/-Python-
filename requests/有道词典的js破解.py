# -*- coding: utf-8 -*-
import json
import random
import hashlib
import time
import requests

def main():
	url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
	headers={
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '242',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': 'P_INFO=lcq19920706@163.com|1582353105|0|other|00&99|anh&1581134759&other#anh&340800#10#0#0|138356&0||lcq19920706@163.com; OUTFOX_SEARCH_USER_ID=1253150999@10.169.0.84; JSESSIONID=aaat1krxVl4cV5P8zQ7bx; OUTFOX_SEARCH_USER_ID_NCOO=1725707764.4605162; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcnb4vARRDmJgoFrd8bx; ___rl__test__cookies=1582629433233',
		'Host': 'fanyi.youdao.com',
		'Origin': 'http://fanyi.youdao.com',
		'Referer': 'http://fanyi.youdao.com/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest'
	
	}
	
	while True:
		## 破解参数 salt,sign,ts,bv.每次取值均发生变化
		
		## salt: i . i = r + parseInt(10 * Math.random(), 10);  r = "" + (new Date).getTime()
		## js中，字符串+数字=字符串
		salt=str(int(time.time()*1000))+str(random.randint(0,9))
		
		## ts: r;   r = "" + (new Date).getTime() [时间戳]
		ts=str(int(time.time()*1000))
		
		## bv:t  t = n.md5(navigator.appVersion) navigator.appVersion 等价 User-Agent
		string='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
		def check(string):
			string=string.encode('utf-8')    ## 编码
			m = hashlib.md5(string).hexdigest()  ## 创建一个md5算法对象，之后无代码提示
			return m
		md5=check(string)
		
		## sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
		#  经过断点调试后，e:需要翻译的文字，i 是 salt
		#  n 是 md5 的类，可以忽略
		e=input('请输入需翻译的英文： ')
		i=salt
		sign_string=check("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
		sign=sign_string
		
		data={
			'i': e,
			'from': 'AUTO',
			'to': 'AUTO',
			'smartresult': 'dict',
			'client': 'fanyideskweb',
			'salt': salt,
			'sign': sign,
			'ts': ts,
			'bv': md5,
			'doctype': 'json',
			'version': '2.1',
			'keyfrom': 'fanyi.web',
			'action': 'FY_BY_CLICKBUTTION',
		
		}
		result=requests.post(url=url,headers=headers,data=data)
		#print(result.text)
		result=result.text
		DATA=json.loads(result)
		print(type(DATA))
		Chinese=DATA['translateResult'][0][0]['tgt']
		English=DATA['translateResult'][0][0]['src']
		print(English,Chinese,sep=' ---> ')
		print()
		entries=DATA['smartResult']['entries']
		sentences=''.join(entries).replace('n.','').strip()
		print(sentences,'\n')

if __name__ == '__main__':
	main()