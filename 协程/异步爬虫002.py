# -*- coding: utf-8 -*-
# @Time : 2020/5/25 11:27
# @Author : Tony
# @File : 异步爬虫002.py
# @Software: PyCharm
# To live is to learn,to learn is to better live.
# Killing time for this


from multiprocessing import Pool
import time
from lxml import etree
import aiohttp
import asyncio

urls = [
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
	'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
]
htmls = []
titles = []
sem = asyncio.Semaphore(10)  # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页html
'''


async def get_html(url, semaphore):
	async with semaphore:
		# async with是异步上下文管理器
		async with aiohttp.ClientSession() as session:  # 获取session
			async with session.get(url) as resp:  # 提出请求
				html = await resp.read()  # 直接获取到bytes
				htmls.append(html)
				print('异步获取%s下的html.' % url)


'''
协程调用方，请求网页
'''


def main_get_html():
	loop = asyncio.get_event_loop()  # 获取事件循环
	tasks = [get_html(url, sem) for url in urls]  # 把所有任务放到一个列表中
	loop.run_until_complete(asyncio.wait(tasks))  # 激活协程
	loop.close()  # 关闭事件循环


'''
	使用多进程解析html

	a+ 以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。
'''


def multi_parse_html(htmls):
	with open(r'数据保存.txt', 'a+') as f:
		j = 0
		for html in htmls:
			title = etree.HTML(html).xpath('//*[@id="title"]/text()')[0]
			f.write(title + '\n')
			j += 1
			print('==== 保存第{}份数据 ====='.format(j))


'''
多进程调用总函数，解析html
'''


def main_parse_html():
	p = Pool(4)
	p.apply_async(multi_parse_html, args=(htmls,))
	p.close()
	p.join()


if __name__ == '__main__':
	start = time.time()
	main_get_html()  # 调用方
	main_parse_html()  # 解析html
	print('总耗时：%.5f秒' % float(time.time() - start))