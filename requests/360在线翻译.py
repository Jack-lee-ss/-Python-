# -*- coding: utf-8 -*-


import json
import re
import requests

def main():
	url = 'http://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=bee%0A'
	headers = {
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
	
	n = input('请输入要翻译的英语： ')
	data = {
		'eng': '1',
		'validate': '',
		'ignore_trans': '0',
		'query': n
	}
	
	result = requests.post(url=url, headers=headers, data=data)
	
	infs = json.loads(result.text)
	
	translation = infs['data']['explain']['translation']
	print(translation)

	examples = infs['data']['explain']['collins']['data']
	Lengths = len((examples))
	print('该单词词性形式共有: %d' % Lengths)
	i=1
	for key,value in examples.items():
		type = key
		print('词性%d：%s' %(i,type))
		contents = examples[type]['datablk']['gramcat'][0]['sensecat'] # 列表

		list_lengths = len(contents)     # 列表长度
		i+=1

		for j in range(list_lengths):
			dir_lengths = len(contents[j])  # 每一个字典的长度

			for key, value in contents[j].items(): # 遍历每一个字典的键
					if "lbcoll"== key:
						if 2==dir_lengths:

							words=contents[j]["lbcoll"][0]
							if "xrefgrp" in contents[j]:
								xrefgrp=contents[j]["xrefgrp"]["xrhw"]
								content=words+' '+xrefgrp
								print(content)

							elif "trangrp" in contents[j]:
								trangrp=contents[j]["trangrp"][0]
								content = words + ' ' + trangrp
								print(content)


						elif 3==dir_lengths:
							words = contents[j]["lbcoll"][0]
							trangrp = contents[j]["trangrp"][0]
							content = words + ' ' + trangrp
							print(content)
							exmplgrp=contents[j]["exmplgrp"][0]
							N_examples = contents[j]['exmplgrp']
							N_examples_length = len(N_examples)
							for x in range(N_examples_length):
								English = N_examples[x]['exmpl'][0]
								Chinese = N_examples[x]['sense'][0]['trangrp'][0]
								examples = English + ' --> ' + Chinese
								print(examples)

					elif "lbsubjfld"==key:
						if 2 == dir_lengths:
							words = contents[j]["lbsubjfld"][0]
							trangrp = contents[j]["trangrp"][0]
							content = words + ' ' + trangrp
							print(content)

						elif 3 == dir_lengths:
							words = contents[j]["lbsubjfld"][0]
							trangrp = contents[j]["trangrp"][0]
							content = words + ' ' + trangrp
							print(content)
							if 'exmplgrp' in contents[j]:
								N_examples = contents[j]['exmplgrp']
								N_examples_length = len(N_examples)
								for x in range(N_examples_length):
									English = N_examples[x]['exmpl'][0]
									Chinese = N_examples[x]['sense'][0]['trangrp'][0]
									examples = English + ' --> ' + Chinese

									print(examples)
							elif 'lbmisc' in contents[j]:
								lbmisc = contents[j]["lbmisc"][0]
								print(lbmisc)



					elif "lbsynonym" == key:

						if 2 == dir_lengths:
							words = contents[j]["lbsynonym"][0]
							trangrp = contents[j]["trangrp"][0]
							content = words + ' ' + trangrp
							print(content)

						elif 3 == dir_lengths:
							words = contents[j]["lbsynonym"][0]
							trangrp = contents[j]["trangrp"][0]
							content = words + ' ' + trangrp
							print(content)
							if 'exmplgrp' in contents[j]:
								N_examples = contents[j]['exmplgrp']
								N_examples_length = len(N_examples)
								for x in range(N_examples_length):
									English = N_examples[x]['exmpl'][0]
									Chinese = N_examples[x]['sense'][0]['trangrp'][0]
									examples = English + ' --> ' + Chinese

									print(examples)
							elif 'lbmisc' in contents[j]:
								lbmisc = contents[j]["lbmisc"][0]
								print(lbmisc)

					elif "phrgrp" == key:
						N_examples = contents[j]['phrgrp']
						N_num_length = len(N_examples)  # 外循环

						for i in range(N_num_length):
							phrgrp = N_examples[i]["phr"][0]  # 句型
							# print('句型: %s'%phrgrp,'\n')
							examples = N_examples[i]['sense'][0]['exmplgrp']
							length = len(examples)  # 内循环
							for j in range(length):
								English_exmpl = examples[j]["exmpl"][0]
								English_exmpl = re.sub(r'<c>', '', English_exmpl)
								English_exmpls = re.sub(r'</c>', '', English_exmpl)
								Chinese_trangrp = examples[j]["sense"][0]["trangrp"][0]
								example = English_exmpls + ' ---> ' + Chinese_trangrp
								print(example,'\n')
						
						
						
						
if __name__ == '__main__':
	main()