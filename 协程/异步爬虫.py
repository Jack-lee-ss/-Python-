# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

## 异步请求单个网页html

import asyncio
import aiohttp
import time

async def get_html(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as result:
			html=await result.text()
			print(html)

def main():
	loop=asyncio.get_event_loop()
	loop.run_until_complete(get_html("https://docs.aiohttp.org/en/stable/client_quickstart.html"))
	loop.close()

if __name__ == "__main__":
	t1=time.time()
	main()
	print(time.time()-t1)


# 多次异步请求url

async def get_url(url,i):
	async with aiohttp.ClientSession() as session :
		async with session.get(url) as result:
			html=await result.text()
			print('第{}次'.format(i))

def main():
	for i in range(10):
		loop=asyncio.get_event_loop()
		loop.run_until_complete(get_url("https://www.baidu.com",i))
		loop.close()

if __name__ == "__main__":
	t=time.time()
	main()
	print(time.time()-t)
	

## 限制并发数量

async def get_urls(url,semaphore):
	async with semaphore:
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as result:
				print(result.status)


def main():
	semaphore=asyncio.Semaphore(50)
	for i in range(100):
		t=time.time()
		loop=asyncio.get_event_loop()
		loop.run_until_complete(get_urls("https://www.baidu.com/",semaphore))
		loop.close()
		print('该次循环用时{}'.format(time.time()-t))


if __name__ == "__main__":
	t2=time.time()
	main()
	print("总耗时{}".format(time.time()-t2))
	

## 异步结合多进程-爬虫程序
'''
	【请求网页】：使用协程。
	【解析HTML】：使用多进程。
'''

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
sem = asyncio.Semaphore(10) # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页html
'''
async def get_html(url):
    with(await sem):
        # async with是异步上下文管理器
        async with aiohttp.ClientSession() as session:  # 获取session
            async with session.get(url) as resp:  # 提出请求
                html = await resp.read() # 直接获取到bytes
                htmls.append(html)
                print('异步获取%s下的html.' % url)

'''
协程调用方，请求网页
'''
def main_get_html():
    loop = asyncio.get_event_loop()           # 获取事件循环
    tasks = [get_html(url) for url in urls]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    loop.close()  # 关闭事件循环
'''
使用多进程解析html
'''
def multi_parse_html(html,cnt):
    title = etree.HTML(html).xpath('//*[@id="title"]/text()')
    titles.append(''.join(title))
    print('第%d个html完成解析－title:%s' % (cnt,''.join(title)))
'''
多进程调用总函数，解析html
'''
def main_parse_html():
    p = Pool(4)
    i = 0
    for html in htmls:
        i += 1
        p.apply_async(multi_parse_html,args=(html,i))
    p.close()
    p.join()


if __name__ == '__main__':
    start = time.time()
    main_get_html()   # 调用方
    main_parse_html() # 解析html
    print('总耗时：%.5f秒' % float(time.time()-start))


## python多进程执行方法apply_async简单使用
#  apply_async是异步非阻塞式，不用等待当前进程执行完毕，随时跟进操作系统调度来进行进程切换，即多个进程并行执行，提高程序的执行效率。
'''
	  python在同一个线程中多次执行同一方法时，该方法执行耗时较长且每次执行过程及结果互不影响，如果只在主进程中执行，效率会很低，因此使用multiprocessing.Pool(processes=n)及其apply_async()方法提高程序执行的并行度从而提高程序的执行效率,其中processes=n为程序并行执行的进程数。
	
	multiprocessing.Pool常用函数解析：

		apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
		close()：关闭Pool，使其不再接受新的任务；
		terminate()：不管任务是否完成，立即终止；
		join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；
'''

import os
import multiprocessing
import time


def write(q):
	print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
	for i in "python":
		q.put(i)


def read(q):
	print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
	for i in range(q.qsize()):
		print("read从Queue获取到消息：%s" % q.get(True))


if __name__ == "__main__":
	print("(%s) start" % os.getpid())
	q = multiprocessing.Manager().Queue()
	po = multiprocessing.Pool()
	po.apply_async(write, args=(q,))

	time.sleep(2)

	po.apply_async(read, args=(q,))
	po.close()
	po.join()
	print("(%s) end" % os.getpid())

###   协程请求网页 + 进程保存数据

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
sem = asyncio.Semaphore(10) # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页html
'''
async def get_html(url):
    with(await sem):
        # async with是异步上下文管理器
        async with aiohttp.ClientSession() as session:  # 获取session
            async with session.get(url) as resp:  # 提出请求
                html = await resp.read() # 直接获取到bytes
                htmls.append(html)
                print('异步获取%s下的html.' % url)

'''
协程调用方，请求网页
'''
def main_get_html():
    loop = asyncio.get_event_loop()           # 获取事件循环
    tasks = [get_html(url) for url in urls]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    loop.close()  # 关闭事件循环

def main_parse_html():
	for html in htmls:
		title = etree.HTML(html).xpath('//*[@id="title"]/text()')
		titles.append(''.join(title))


def save():
	with open(r'数据保存.txt','wb') as f:
		for i in titles:
			f.write(i.encode()+b'\n')
			print('..... 保存一份 .....')

if __name__ == '__main__':
	t=time.time()
	main_get_html()   # 调用方
	main_parse_html() # 解析html
	save()
	print('总耗时：%.5f秒' % float(time.time()-t))



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
sem = asyncio.Semaphore(10) # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页html
'''
async def get_html(url,semaphore):
    async with semaphore:
        # async with是异步上下文管理器
        async with aiohttp.ClientSession() as session:  # 获取session
            async with session.get(url) as resp:  # 提出请求
                html = await resp.read() # 直接获取到bytes
                htmls.append(html)
                print('异步获取%s下的html.' % url)

'''
协程调用方，请求网页
'''
def main_get_html():
    loop = asyncio.get_event_loop()           # 获取事件循环
    tasks = [get_html(url,sem) for url in urls]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    loop.close()  # 关闭事件循环
'''
	使用多进程解析html
	
	a+ 以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。
'''

def multi_parse_html(htmls):
	with open(r'数据保存.txt','a+') as f:
		j=0
		for html in htmls:
			title = etree.HTML(html).xpath('//*[@id="title"]/text()')[0]
			f.write(title+'\n')
			j+=1
			print('==== 保存第{}份数据 ====='.format(j))
	
'''
多进程调用总函数，解析html
'''
def main_parse_html():
	p = Pool(4)
	p.apply_async(multi_parse_html,args=(htmls,))
	p.close()
	p.join()
	
if __name__ == '__main__':
	start = time.time()
	main_get_html()   # 调用方
	main_parse_html() # 解析html
	print('总耗时：%.5f秒' % float(time.time()-start))