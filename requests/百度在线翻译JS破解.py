# -*- coding: utf-8 -*-
import json
import random
import hashlib
import time
import requests
import execjs

def main():
	url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
	headers={
		'origin': 'https://fanyi.baidu.com',
		'referer': 'https://fanyi.baidu.com/?aldtype=16047',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
		'cookie': 'BAIDUID=135C20AE67CC6E4B79982B53843A8A2A:FG=1; BDUSS=NZbktZbXNuazlLc2dhZUJyMm1OS344VlIzNlM3fkVnbk90d2UwY1puRjUybUZlSVFBQUFBJCQAAAAAAAAAAAEAAACXYk1A0rnAtMPJzbfLrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHlNOl55TTpeZz; BIDUPSID=135C20AE67CC6E4B79982B53843A8A2A; PSTM=1580881126; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=HSIsJeCCxG3HJ3TuoCRPSZHdwIbS8AzZG2BK3J; H_BDCLCKID_SF=tRk8oCPKtKvbfP0kb4Q_bICShUFse4RC-2Q-5hOy3KO1OCO25tnTjUDyWGoHBxcaLbbCXfcTtqovhpFuDjtBDjvBDNRf-b-X5D6X05rJabC3hUOGKU6qLUtbQNb7BjJnbCOmhf3PfpTFjhvP0T7N2lI1D45iJMIEtRk8oCPKtKvbfP0kb4Q_bICShUFsBpJA-2Q-5hOy3KO1OCO25tnT0l89W47b-McaLbbCXfcTtqovhpFu-n5jHjQyjH8H3J; delPer=0; PSINO=6; cflag=13%3A3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=30748_1433_21087_30839_30794_30823_26350_22158; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1582719140; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1582719140; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_3ede485da069f08cf1d7b53ddd92559ff52f_300_1582718995185_36.57.28.75_2a41d48b; yjs_js_security_passport=c7d050377d784d997b7c702d21e2b1815616ba09_1582718995_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
		# ':authority': 'fanyi.baidu.com',
		# ':method': 'POST',
		# ':path': '/v2transapi?from=en&to=zh',
		# ':scheme': 'https',
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'content-length': '138',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
		
	}
	
	## 参数变化  sign:
	n=input('请输入英文： ')
	with open(r'F:\python代码\Python 基本操作\requests\JS脚本\百度翻译2.js','r',encoding='utf-8') as f:
		
		jsdata=f.read()
	dat=execjs.compile(jsdata).call('e',n)
	print('=======')
	
	data={
		'from': 'en',
		'to': 'zh',
		'query': n,
		'transtype': 'translang',
		'simple_means_flag': '3',
		'sign': dat,
		'token': '70418c88e35138dc482215600822fe39',
		'domain': 'common'
	}
	print('-----')
	result=requests.post(url=url,headers=headers,data=data)
	print(result.text.encode('utf-8').decode('unicode_escape'))
	


if __name__ == '__main__':
	main()