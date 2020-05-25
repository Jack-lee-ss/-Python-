# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

## call_soon，即刻执行
# import asyncio
#
# def callback(sleep_times):
# 	print("sleep{}success".format(sleep_times))
#
# def stoploop(loop):
# 	loop.stop()
#
# if __name__ == "__main__":
# 	loop=asyncio.get_event_loop()
# 	loop.call_soon(callback,2)
# 	loop.call_soon(stoploop,loop)
# 	loop.run_forever()
#
# '''
# 	原因：run_until_complete和run_forever运行对比.
# 	run_until_complete 来运行 loop ，等到 future 完成，run_until_complete 也就返回了。
# 	run_forever 会一直运行，直到 stop 被调用（在python3.7中已经取消了）
# '''
#
# ## call_later，指定时间之后再运行，执行的顺序和指定的时间有关，cal_soon比call_later优先执行
#
# import asyncio
#
# def callback(sleep_times):
# 	print('sleep {} success'.format(sleep_times))
#
# def stop_loop(loop):
# 	loop.stop()
#
# if __name__ == '__main__':
# 	loop = asyncio.get_event_loop()
# 	# 指定时间之后再运行
# 	loop.call_later(1, callback, 1)
# 	loop.call_later(2, callback, 2)
# 	loop.call_later(3, callback, 3)
# 	# loop.call_soon(stop_loop, loop)
# 	loop.run_forever()

## aiohttp:高并发异步爬虫
## asyncio和Python的异步HTTP客户端/服务器

# import aiohttp
# import asyncio
#
# async def fetch(url):
# 	async with aiohttp.ClientSession() as session:
# 		try:
# 			async with session.get(url) as resp:
# 				print("url status: {}".format(resp.status))
# 				if resp.status in [200,201]:
# 					data=await resp.text()
# 					return data
# 		except Exception as e:
# 			print(e)
# loop=asyncio.get_event_loop()
# loop.run_until_complete(fetch("http://www.jobbole.com/"))
#
#
# import aiohttp
# import asyncio
#
# async def fetch(session, url):
# 	async with session.get(url) as response:
# 		return await response.text()
#
# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		html = await fetch(session, 'http://httpbin.org/headers')
# 		print(html)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


## 获取网页html文档
# import asyncio
# import aiohttp
#
# async def get_html(session, url):
# 	try:
# 		async with session.request('GET',url) as response:
# 			if response.status == 200:
# 				return await response.text()
# 	except Exception as e:
# 		print(e)
#
#
# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		html= await get_html(session,"https://www.baidu.com")
# 		print(html)
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(main())
#
#
# # import requests
# # res=requests.get("https://www.baidu.com/").content.decode('utf-8')
# # print(res)

### 普通爬虫请求网页：
import time
from lxml import etree
import requests

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
'''
提交请求获取AAAI网页,并解析HTML获取title
'''


def get_title(url, cnt):
	response = requests.get(url)  # 提交请求,获取响应内容
	html = response.content  # 获取网页内容(content返回的是bytes型数据,text()获取的是Unicode型数据)
	title = etree.HTML(html).xpath('//*[@id="title"]/text()')  # 由xpath解析HTML
	print('第%d个title:%s' % (cnt, ''.join(title)))


if __name__ == '__main__':
	start1 = time.time()
	i = 0
	for url in urls:
		i = i + 1
		start = time.time()
		get_title(url, i)
		print('第%d个title爬取耗时:%.5f秒' % (i, float(time.time() - start)))
	print('爬取总耗时:%.5f秒' % float(time.time() - start1))


## 基于协程的异步爬虫程序

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
titles = []
sem = asyncio.Semaphore(10) # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页,并解析HTML获取title
'''
async def get_title(url):
	#with(await sem):
	# async with是异步上下文管理器
	async with aiohttp.ClientSession() as session:  # 获取session
		async with session.request('GET', url) as resp:  # 提出请求
			# html_unicode = await resp.text()
			# html = bytes(bytearray(html_unicode, encoding='utf-8'))
			html = await resp.read() # 可直接获取bytes
			title = etree.HTML(html).xpath('//*[@id="title"]/text()')
			print(''.join(title))
'''
调用方
'''
def main():
	loop = asyncio.get_event_loop()           # 获取事件循环
	tasks = [get_title(url) for url in urls]  # 把所有任务放到一个列表中
	loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
	loop.close()  # 关闭事件循环

if __name__ == '__main__':
	start = time.time()
	main()  # 调用方
	print('总耗时：%.5f秒' % float(time.time()-start))
