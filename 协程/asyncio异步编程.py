# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

# import asyncio
# import time
# async def get_html(url):
# 	print('start get url')
# 	await asyncio.sleep(2)
# 	#time.sleep(2)
# 	print("end get url")
#
# if __name__=="__main__":
# 	start_time=time.time()
# 	loop=asyncio.get_event_loop()
# 	tasks=[get_html("http://www.baidu.com") for i in range(10)]
# 	loop.run_until_complete(asyncio.wait(tasks))
# 	print(time.time()-start_time)

'''
	异步协程:
		1. event_loop:事件循环，loop就是这个持续不断的监视器。
		相当于一个无限循环。我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。程序是按照设定的顺序从头执行到尾，运行的次数也是完全按照设定。在编写程序时，如果有一部分程序的运行耗时是比较久的，需要先让出其控制权，让它在后台运行，其它的程序可以先运行起来。当后台运行的程序完成后，也需要及时通知主程序已经完成任务可以进行下一步操作，但这个过程所需的时间是不确定的，需要主程序不断的监听状态，一旦收到了任务完成的消息，就开始进行下一步。
		
		2. coroutine:协程对象类型.
		使用 async 关键字来定义的方法在调用时不会立即执行，而是返回一个协程对象。
		
		3. task:任务.
		它是对协程对象的进一步封装，包含了任务的各个状态，比如 running、finished 等，可以用这些状态来获取协程对象的执行情况。
		
		4. future.
		代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。通过 asyncio 的 ensure_future() 方法也可以返回一个 task 对象，这样可以不借助于 loop 来定义。
		
		5. 绑定回调.
		可以为某个 task 绑定一个回调方法。

'''
# 首先引入 asyncio 包，这样才能使用 async 和 await
import asyncio

# 使用 async 定义一个 execute 方法，接收一个参数并打印
async def execute(x):
	print("Number = ", x)

# 此时调用 execute 函数并不会执行，而是返回一个协程对象
coroutine = execute(1)
print("coroutine:", coroutine)
print("After calling execute.")

# 然后使用 get_event_loop 方法创建一个事件循环 loop
loop = asyncio.get_event_loop()
# 之后调用 loop 对象的 run_until_complete 方法将协程对象注册到事件循环 loop 中并启动，函数才能运行
loop.run_until_complete(coroutine)
print("After calling loop.")
print('===============')

import asyncio

async def execute(x):
	print("Number = ", x)
	return x

if __name__ == '__main__':
	coroutine = execute(1)
	print("Coroutine:", coroutine)
	print("After calling execute.")
	
	loop = asyncio.get_event_loop()         ## 定义时件循环
	task = loop.create_task(coroutine)       # 循环中设置任务
	print("Task:", task)
	
	loop.run_until_complete(task)            # 运行完成任务,打印出 print("Number = ", x)
	print("Task:", task)
	print("After calling loop.")
print('+++++++++++++++')

import asyncio

async def execute(x):
	print("Number = ", x)

if __name__ == '__main__':
	coroutine = execute(1)
	task = asyncio.ensure_future(coroutine)    # 等价于设置事件任务
	print("Task:", task,'\n')                  # 开始执行情况
	
	loop = asyncio.get_event_loop()
	print("Task:", task)
	loop.run_until_complete(task)
	print("Task:", task)
	print("After calling loop.",'\n')

print('***********************')

# import asyncio
# import requests
#
# async def request():
# 	url = "https://www.baidu.com"
# 	status = requests.get(url=url).status_code
# 	return status
#
# def callback(task):
# 	print("Status:", task.result())
#
# if __name__ == '__main__':
# 	coroutine = request()
# 	task = asyncio.ensure_future(coroutine)
# 	task.add_done_callback(callback)
# 	print("Task:", task)
#
# 	loop = asyncio.get_event_loop()
# 	loop.run_until_complete(task)
# 	print("Task:", task)

import asyncio

def callback(task):
	print('i am callback:',task.result())

async def hello(name):
	print('hello to :',name)
	return name

c = hello('bobo')

task = asyncio.ensure_future(c)
#给任务对象绑定一个回调函数
task.add_done_callback(callback)
loop.run_until_complete(task)


# import time
# import asyncio
# import requests
#
#
# async def getPage(name, url):
# 	print("正在爬取%s......" % name)
# 	response = requests.get(url=url).text
# 	with open("%s.html" % name, "w", encoding="utf-8") as fp:
# 		fp.write(response)
# 	print("%s爬取完毕......" % name)
#
#
# if __name__ == '__main__':
# 	startTime = time.time()
# 	urlDict = {
# 		"百度搜索": "https://www.baidu.com/",
# 		"百度翻译": "https://fanyi.baidu.com/",
# 		"CSDN": "https://www.csdn.net/",
# 		"博客园": "https://www.cnblogs.com/",
# 		"哔哩哔哩": "https://www.bilibili.com/",
# 		"码云": "https://gitee.com/",
# 		"拉勾网": "https://www.lagou.com/",
# 	}
# 	taskList = []
# 	for key, value in urlDict.items():
# 		request = getPage(key, value)
# 		task = asyncio.ensure_future(request)
# 		taskList.append(task)
#
# 	loop = asyncio.get_event_loop()
# 	loop.run_until_complete(asyncio.wait(taskList))
# 	print("Time consuming:", time.time() - startTime)
# 	# Time consuming: 2.432551383972168

# import time
# import asyncio
# import aiohttp
#
# async def getPage(name, url):
# 	print("正在爬取%s......" % name)
# 	async with aiohttp.ClientSession() as session:
# 		async with await session.get(url) as response:
# 			responseText = await response.text()
# 			save(name, responseText)
# 	print("%s爬取完毕......" % name)
#
#
# def save(name, response):
# 	with open("%s.html" % name, "w", encoding="utf-8") as fp:
# 		fp.write(response)
#
#
# if __name__ == '__main__':
# 	startTime = time.time()
# 	urlDict = {
# 		"百度搜索": "https://www.baidu.com/",
# 		"百度翻译": "https://fanyi.baidu.com/",
# 		"CSDN": "https://www.csdn.net/",
# 		"博客园": "https://www.cnblogs.com/",
# 		"哔哩哔哩": "https://www.bilibili.com/",
# 		"码云": "https://gitee.com/",
# 		"拉勾网": "https://www.lagou.com/",
# 	}
# 	taskList = []
# 	for key, value in urlDict.items():
# 		request = getPage(key, value)
# 		task = asyncio.ensure_future(request)
# 		taskList.append(task)
#
# 	loop = asyncio.get_event_loop()
# 	loop.run_until_complete(asyncio.wait(taskList))
# 	print("Time consuming:", time.time() - startTime)
# 	## Time consuming: 1.6499879360198975


### asyncio.gather():gather 可以将任务分组，一般优先使用 gather。在某些定制化任务需求的时候，会使用 wait。

# import asyncio
# import time
#
# # 并发执行协程
# # 模拟的耗时任务 交给协程来处理
# async def my_task(name, number):
# 	await asyncio.sleep(number)
# 	print('%s 已经完成任务...' % name)
#
# async def main():
# 	print(f"started at {time.strftime('%X')}")
#
# # 将三个任务交给 asyncio.gather 并发的执行 理论的预期：并行耗时应该为 4秒，否则为未达到预期
# 	await asyncio.gather(
#         my_task('A', 2),
#         my_task('B', 3),
#         my_task('C', 4),
#     )
#
# 	# 下面的方法和上面可以达到相同的预期 但是 在启动协程较多的情况下 推荐使用上法
# 	# task1 = asyncio.create_task(my_task('A', 2))
# 	# task2 = asyncio.create_task(my_task('B', 3))
# 	# task3 = asyncio.create_task(my_task('C', 4))
# 	# await task1
# 	# await task2
# 	# await task3
# 	print(f"finished at {time.strftime('%X')}")
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(main())


####  asyncio.wait(tasks)，asyncio.gather(tasks)
import asyncio
import time
async def get_html(sleep_times):
	print('waiting...')
	await asyncio.sleep(sleep_times)
	print("done after {}s".format(sleep_times))
	
if __name__ == "__main__":
	task1 = get_html(2)
	task2 = get_html(3)
	task3 = get_html(3)
	tasks=[task1,task2,task3]   ## 创建三个任务
	loop=asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))  ## asyncio.wait(tasks) 可以迭代任务

import asyncio
import time

now = lambda: time.time()
async def do_some_work(x):
	print("waiting:",x)
	await asyncio.sleep(x)
	return "Done after {}s".format(x)

async def main():
	coroutine1 = do_some_work(1)
	coroutine2 = do_some_work(2)
	coroutine3 = do_some_work(4)
	tasks = [
		asyncio.ensure_future(coroutine1),
		asyncio.ensure_future(coroutine2),
		asyncio.ensure_future(coroutine3)
	]
	return await asyncio.gather(*tasks)

start = now()

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
for result in results:
	print("Task ret:",result)

print("Time:", now()-start)


import asyncio
import time


now = lambda: time.time()

async def do_some_work(x):
	print("waiting:",x)
	await asyncio.sleep(x)
	return "Done after {}s".format(x)

async def main():
	coroutine1 = do_some_work(1)
	coroutine2 = do_some_work(2)
	coroutine3 = do_some_work(4)
	tasks = [
		asyncio.ensure_future(coroutine1),
		asyncio.ensure_future(coroutine2),
		asyncio.ensure_future(coroutine3)
	]
	return await asyncio.wait(tasks)

start = now()

loop = asyncio.get_event_loop()
done,pending = loop.run_until_complete(main())
for task in done:
	print("Task ret:",task.result())

print("Time:", now()-start)

## 协程的停止
'''
	future对象有几个状态：
		Pending
		Running
		Done
		Cacelled
		创建future的时候，task为pending，事件循环调用执行的时候当然就是running，调用完毕自然就是done，如果需要停止事件循环，就需要先把task取消。可以使用asyncio.Task获取事件循环的task.
		
'''

import asyncio
import time


now = lambda :time.time()


async def do_some_work(x):
	print("Waiting:",x)
	await asyncio.sleep(x)
	return "Done after {}s".format(x)

coroutine1 =do_some_work(1)
coroutine2 =do_some_work(2)
coroutine3 =do_some_work(2)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

start = now()

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
	print(asyncio.Task.all_tasks())
	for task in asyncio.Task.all_tasks():
		print(task.cancel())
	loop.stop()
	loop.run_forever()
finally:
	loop.close()

print("Time:",now()-start)
## 启动事件循环之后，马上ctrl+c，会触发run_until_complete的执行异常 KeyBorardInterrupt。然后通过循环asyncio.Task取消future.True表示cannel成功，loop stop之后还需要再次开启事件循环，最后在close，不然还会抛出异常.循环task，逐个cancel是一种方案，可是正如上面我们把task的列表封装在main函数中，main函数外进行事件循环的调用。这个时候，main相当于最外出的一个task，那么处理包装的main函数即可.


## 循环嵌套：
import asyncio
async def compute(x,y):
	print("Computer %s + %s ..."%(x,y))
	await asyncio.sleep(1.0)
	return x+y
async def print_sum(x,y):
	result=await compute(x,y)
	print("%s + %s = %s"%(x, y, result))
loop=asyncio.get_event_loop()
loop.run_until_complete(print_sum(1,2))
loop.close()
