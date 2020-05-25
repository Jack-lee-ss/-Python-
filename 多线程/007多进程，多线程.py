# -*- coding: utf-8 -*-

### 单线程
# import time
# import os
#
# def long_time_task():
#     print('当前进程: {}'.format(os.getpid()))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
# if __name__ == "__main__":
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     for i in range(2):
#         long_time_task()
#
#     end = time.time()
#     print("用时{}秒".format((end-start)))


## 多进程：并发执行的时间明显比顺序执行要快很多。你还可以看到尽管我们只创建了两个进程，可实际运行中却包含里1个母进程和2个子进程。之所以我们使用join()方法就是为了让母进程阻塞，等待子进程都完成后才打印出总共耗时，否则输出时间只是母进程执行的时间。

# from multiprocessing import Process
# import os
# import time
#
# def long_time_task(i):
#     print('子进程: {} - 任务{}'.format(os.getpid(), i))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
# if __name__=='__main__':
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     p1 = Process(target=long_time_task, args=(1,))
#     p2 = Process(target=long_time_task, args=(2,))
#     print('等待所有子进程完成。')
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))
##：新创建的进程与进程的切换都是要耗资源的，所以平时工作中进程数不能开太大。同时可以运行的进程数一般受制于CPU的核数。

## 利用multiprocess模块的Pool类创建多进程
# 可以通过传递参数限制并发进程的数量，默认值为CPU的核数。Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果进程池还没有满，就会创建一个新的进程来执行请求。如果池满，请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求。

# 1.apply_async()
# 函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]]) 其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。这是默认方式。

# 2.map()
# 函数原型：map(func, iterable[, chunksize=None]) Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。

# 3.close()
# 关闭进程池（pool），使其不在接受新的任务

# 4.join()
#主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用

## 下例是一个简单的multiprocessing.Pool类的实例。因为我的CPU是4核的，一次最多可以同时运行4个进程，所以我开启了一个容量为4的进程池。4个进程需要计算5次，你可以想象4个进程并行4次计算任务后，还剩一次计算任务(任务4)没有完成，系统会等待4个进程完成后重新安排一个进程来计算

# from multiprocessing import Pool, cpu_count
# import os
# import time
#
# def long_time_task(i):
#     print('子进程: {} - 任务{}'.format(os.getpid(), i))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
# if __name__=='__main__':
#     print("CPU内核数:{}".format(cpu_count()))
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有子进程完成。')
#     p.close()
#     p.join()
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))
	
## 多线程使用queue队列通信-经典的生产者和消费者模型
# 创建了两个线程，一个负责生成，一个负责消费，所生成的产品存放在queue里，实现了不同线程间沟通

# from queue import Queue
# import random, threading, time
#
# # 生产者类
# class Producer(threading.Thread):
#     def __init__(self, name, queue):
#         threading.Thread.__init__(self, name=name)
#         self.queue = queue
#
#     def run(self):
#         for i in range(1, 5):
#             print("{} is producing {} to the queue!".format(self.getName(), i))
#             self.queue.put(i)
#             time.sleep(random.randrange(10) / 5)
#         print("%s finished!" % self.getName())
#
#
# # 消费者类
# class Consumer(threading.Thread):
#     def __init__(self, name, queue):
#         threading.Thread.__init__(self, name=name)
#         self.queue = queue
#
#     def run(self):
#         for i in range(1, 5):
#             val = self.queue.get()
#             print("{} is consuming {} in the queue.".format(self.getName(), val))
#             time.sleep(random.randrange(10))
#         print("%s finished!" % self.getName())
#
#
# def main():
#     queue = Queue()
#     producer = Producer('Producer', queue)
#     consumer = Consumer('Consumer', queue)
#
#     producer.start()
#     consumer.start()
#
#     producer.join()
#     consumer.join()
#     print('All threads finished!')
#
# if __name__ == '__main__':
	
    # main()
## Python多进程和多线程哪个快?

# 由于GIL的存在，很多人认为Python多进程编程更快，针对多核CPU，理论上来说也是采用多进程更能有效利用资源。 网上很多人已做过比较，我直接告诉你结论吧。对CPU密集型代码(比如循环计算) - 多进程效率更高对IO密集型代码(比如文件操作，网络爬虫) - 多线程效率更高。为什么是这样呢？其实也不难理解。对于IO密集型操作，大部分消耗时间其实是等待时间，在等待时间中CPU是不需要工作的，那你在此期间提供双CPU资源也是利用不上的，相反对于CPU密集型代码，2个CPU干活肯定比一个CPU快很多。那么为什么多线程会对IO密集型代码有用呢？这时因为python碰到等待会释放GIL供新的线程使用，实现了线程间的切换。

### 单线程下载图片

import os
import re
import time

from lxml import etree
import requests
from urllib import request
#
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
#
# def get_url(url, x):
# 	i = 1
# 	reponse = requests.get(url=url, headers=headers)
# 	html = reponse.text
# 	img_urls = etree.HTML(html)
# 	infos = img_urls.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
# 	for imgs in infos:
# 		img = imgs.get('data-original')
# 		#print(img)
# 		alt = imgs.get('alt')
# 		alt = re.sub(r'[\\?？\.!(N)\*0:]', '', alt)
# 		a = os.path.splitext(img)[1]  ## 分割文件与后缀名
# 		file = alt + a  # 拼出文件名
# 		#print(file)
# 		request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + file)  # 保存图片并且给图片起名
# 		print('===========保存第%s页第%s张============' % (x, i))
# 		i += 1
#
# def main():
# 	start_page = int(input('请输入起始页码：'))
# 	end_page = int(input('请输入结束页码：'))
# 	t_start = time.time()
# 	for x in range(start_page, end_page + 1):
# 		url = 'http://www.doutula.com/photo/list/?page=' + str(x)
# 		li=get_url(url, x)  # 获取 地址
# 	t_end = time.time()
#
# 	print("总共用时{}秒".format((t_end - t_start)))
#
# if __name__ == '__main__':
# 	main()





##   多线程下图片
import threading
import time
from queue import Queue

headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}

def  get_url(q,start_page,end_page):
	for x in range(start_page, end_page + 1):
		url = 'http://www.doutula.com/photo/list/?page=' + str(x)
		reponse = requests.get(url=url, headers=headers)
		html = reponse.text
		img_urls = etree.HTML(html)
		infos = img_urls.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
		for imgs in infos:
			img = imgs.get('data-original')
			alt = imgs.get('alt')
			alt = re.sub(r'[\\?？\.!(N)\*0:]', '', alt)
			a = os.path.splitext(img)[1]  ## 分割文件与后缀名
			file = alt + a  # 拼出文件名
			#print(file)
			q.put((img,file))


def download_pic(q):
	i=0
	while True:
		img,file=q.get()
		request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + file)  # 保存图片并且给图片起名
		i+=1
		print('===========已经保存第%s张============' % i)
		if q.empty():
			break

def main():
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	t_start=time.time()
	q=Queue(100)
	t1=threading.Thread(target=get_url,args=(q,start_page,end_page))
	t2=threading.Thread(target=download_pic,args=(q,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	t_end=time.time()
	print("总共用时{}秒".format((t_end - t_start)))

if __name__== '__main__':
	main()

## 多进程下载图片
# from  multiprocessing import Queue
# import multiprocessing
# import time
# from queue import Queue
#
# headers={
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
#
# def  get_url(q,start_page,end_page):
# 	for x in range(start_page, end_page + 1):
# 		url = 'http://www.doutula.com/photo/list/?page=' + str(x)
# 		reponse = requests.get(url=url, headers=headers)
# 		html = reponse.text
# 		img_urls = etree.HTML(html)
# 		infos = img_urls.xpath('//div[@class="random_picture"]//img[@class!="gif"]')
# 		for imgs in infos:
# 			img = imgs.get('data-original')
# 			alt = imgs.get('alt')
# 			alt = re.sub(r'[\\?？\.!(N)\*0:]', '', alt)
# 			a = os.path.splitext(img)[1]  ## 分割文件与后缀名
# 			file = alt + a  # 拼出文件名
# 			#print(file)
# 			q.put((img,file))
#
# def download_pic(q):
# 	i=0
# 	while True:
# 		img,file=q.get()
# 		request.urlretrieve(img, 'F:/python代码/爬虫/doutuba/' + file)  # 保存图片并且给图片起名
# 		i+=1
# 		print('===========已经保存第%s张============' % i)
# 		if q.empty():
# 			break
#
# def main():
# 	start_page = int(input('请输入起始页码：'))
# 	end_page = int(input('请输入结束页码：'))
# 	t_start=time.time()
# 	q=multiprocessing.Queue(100)
# 	t1=multiprocessing.Process(target=get_url,args=(q,start_page,end_page))
# 	t2=multiprocessing.Process(target=download_pic,args=(q,))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	t_end=time.time()
# 	print("总共用时{}秒".format((t_end - t_start)))
#
# if __name__== '__main__':
# 	main()

