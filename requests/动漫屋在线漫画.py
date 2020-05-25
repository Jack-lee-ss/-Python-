# -*- coding: utf-8 -*-
import requests

def main():
	start_page=int(input('请输入起始页：'))
	end_page=int(input('请输入结束页（小于100）： '))
	headers={
		'Referer': 'http://www.dm5.com/m9835/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
	}
	for i in range(start_page,end_page+1):
		url='http://manhua1014-61-174-50-99.cdndm5.com/l/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B[%E7%AF%AE%E7%90%83%E9%A3%9E%E4%BA%BA]/%E6%A8%BD%E7%AF%AE%E9%AB%98%E6%89%8B1/slamdunk_01_%d.jpg?cid=9835&key=0c6c9a083d66cba3d01b83c79998f9a9&uk='
		if i<10:

			url='http://manhua1014-61-174-50-99.cdndm5.com/l/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B[%E7%AF%AE%E7%90%83%E9%A3%9E%E4%BA%BA]/%E6%A8%BD%E7%AF%AE%E9%AB%98%E6%89%8B1/slamdunk_01_00'+str(i)+'.jpg?cid=9835&key=0c6c9a083d66cba3d01b83c79998f9a9&uk='

		elif i<100:
			url='http://manhua1014-61-174-50-99.cdndm5.com/l/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B[%E7%AF%AE%E7%90%83%E9%A3%9E%E4%BA%BA]/%E6%A8%BD%E7%AF%AE%E9%AB%98%E6%89%8B1/slamdunk_01_0'+str(i)+'.jpg?cid=9835&key=0c6c9a083d66cba3d01b83c79998f9a9&uk='

		else:
			url='http://manhua1014-61-174-50-99.cdndm5.com/l/%E7%81%8C%E7%AF%AE%E9%AB%98%E6%89%8B[%E7%AF%AE%E7%90%83%E9%A3%9E%E4%BA%BA]/%E6%A8%BD%E7%AF%AE%E9%AB%98%E6%89%8B1/slamdunk_01_100.jpg?cid=9835&key=0c6c9a083d66cba3d01b83c79998f9a9&uk='

		from contextlib import closing
		with closing(requests.get(url=url, headers=headers, stream=True)) as result:  ## 关闭
			with open('./picts/00'+str(i)+'.png', 'wb')as f:
				for chunk in result.iter_content(128):
					f.write(chunk)
			print('============')


if __name__ == '__main__':
	main()




