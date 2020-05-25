# -*- coding: utf-8 -*-
import json
import re
import requests

def main():
	url='http://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=bee%0A'
	headers={
		'Accept': 'application/json, text/plain, */*',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Cookie': 'Q_UDID=da026a52-a593-cead-8495-1a11fcb3f0d6; __guid=144965027.1173632394707392300.1582726101283.9526; count=1',
		'Host': 'fanyi.so.com',
		'Origin': 'http://fanyi.so.com',
		'pro': 'fanyi',
		'Referer': 'http://fanyi.so.com/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
	}
	
	n=input('请输入要翻译的英语： ')
	data={
		'eng': '1',
		'validate': '',
		'ignore_trans': '0',
		'query': n
	}
	
	result=requests.post(url=url,headers=headers,data=data)
	
	infs=json.loads(result.text)
	
	translation = infs['data']['explain']['translation']
	
	
	examples=infs['data']['explain']['collins']['data']
	Lengths=len((examples))
	print('该单词词性形式共有: %d'%Lengths)
	
	for i in range(Lengths):
		type=examples[i]
		print(type)
	
	contents=examples['n']['datablk']['gramcat'][0]['sensecat']
	N_num_lengths=len(contents)
	
	for j in range(N_num_lengths):
		for key ,value in contents[j].items():
			if "trangrp"==key:
				#print(contents[j]["trangrp"][0])
				content=contents[j]["trangrp"][0]
				#print(content)
				
				if "exmplgrp"==key:
					N_examples = contents[0]['exmplgrp']
					N_num_length = len(N_examples)
					for i in range(N_num_length):
						English=N_examples[i]['exmpl'][0]
						Chinese=N_examples[i]['sense'][0]['trangrp'][0]
						examples=English+' --> '+Chinese
						#print(examples)
	
				
			elif "phrgrp"==key:
				N_examples = examples['n']['datablk']['gramcat'][0]['sensecat'][j]['phrgrp']
				N_num_length = len(N_examples)   # 外循环
				
				for i in range(N_num_length):
					phrgrp = N_examples[i]["phr"][0]  # 句型
					#print('句型: %s'%phrgrp,'\n')
					examples=N_examples[i]['sense'][0]['exmplgrp']
					length = len(examples)  # 内循环
					for j in range(length):
						English_exmpl=examples[j]["exmpl"][0]
						English_exmpl=re.sub(r'<c>','',English_exmpl)
						English_exmpls=re.sub(r'</c>','',English_exmpl)
						Chinese_trangrp=examples[j]["sense"][0]["trangrp"][0]
						example=English_exmpls+' ---> '+Chinese_trangrp
						#print(example,'\n')
			
			elif "lbsubjfld"==key:
				content1=contents[j]["lbsubjfld"][0]
				content2=contents[j]["trangrp"][0]
				content=content1+content2
				print('词义：%s'%content)
				examples=contents[j]["exmplgrp"]
				lengths=len(examples)
				
				for i in range(lengths):
					if examples[i]["sense"][0]["trangrp"][0] is None:
						print('')
					else:
						English_exmpl=examples[i]["exmpl"][0]
						Chinese_trangrp=examples[i]["sense"][0]["trangrp"][0]
						example=English_exmpl+' ---> '+Chinese_trangrp
						print(example)

		
	
	#
	

if __name__ == '__main__':
	main()