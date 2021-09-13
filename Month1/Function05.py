#函数：装饰模式
import random
import functools
'''
真实函数
装饰函数——>装饰真实函数
调用装饰器

#真实函数
def meet_mayun():
	print('你好，马云')
#装饰函数
def decorator(func):
	def inner():
		if random.randint(1,8)<5:
			func()
		else:
			print('不好意思')
	return inner

dec = decorator(meet_mayun)
dec()
'''
#装饰器
def deco(func):
	@functools.wraps(func)
	def inner():
		if random.randint(1,8)<5:
			func()
		else:
			print('不好意思')
	return inner
@deco
def meet_mayun():
	print('你好马云')

@deco
def meet_mahuateng():
	print('你好马化腾')

meet_mayun()
meet_mahuateng()
