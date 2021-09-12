from functools import reduce#alt+回车
'''
#函数
函数名就是引用，构建函数时，我们的函数名其实就是对这个函数的一个引用而已
函数名是对函数的引用，我们可以为同一个函数分配多个名称

def demo():
	print('函数引用')

print(id(demo))
print(type(demo))
a=demo#这个就是引用，del只会删掉引用
print(id(a))
print(type(a))
del demo
a()
b=a
b()

#函数传递
def a():
	print('这是a函数')
def b():
	print('这是b函数')
def c(func):
	print('这是一个可以调用其他函数的函数')
	func()
c(a)#c(b)

def f(_list):
	r=[]
	for i in _list:
		r.append(i**i)
	return r
def m(func,_list):#方法的名字就是一个引用
	return func(_list)
print(m(f,[1,2,3]))

def r(*args):
	r=['apple','banana','orange'][len(args)-1]
	return r
def d(func,*args):
	print('eat a '+func(*args))

d(r,'asd','asd','dsa')

#高级函数
def square(x):
	return x * x
r=map(square,[1,2,3,4,5])
print(list(r))
r=map(str,[1,2,3,4,5])
print(list(r))


def plus(x, y):
	return x + y

r = reduce(plus, [1, 2, 3, 4, 5])
print(r, type(r))

def paste_num(x,y):
	return x*10+y
r=reduce(paste_num,[1,2,3,4,5])
print(r)

def compare(x):
	return x>20
r=filter(compare,[12,23,34,45,56])
print(list(r))

# 返回函数
def demo():
	def haha():
		print('函数作为返回值返回')
	return haha
# x=demo()
# x()
demo()()
def outter(*args):
	print("外函数执行...") # 转成字符串
	def inner():
		print("内函数执行...")
		print(",".join(map(str, args)))
	return inner
print(*[1,2,3,4])
t = outter(*[1,2,3,4]) # *拆箱
print(t)
t()


# 递归

	5! = 1*2*3*4*5 = 4!*5
	4! = 1*2*3*4 = 3!*4
	3! = 1*2*3 = 2!*3
	2! = 1*2 = 1!*2
	1! = 1

def product(n):
	if n <= 0:
		return 1
	return product(n-1) * n
print(product(5))

fib1 fib2 fib3 fib4 fib5 fib6 fib7 fib8
1 1 2 3 5 8 13 21

def fib(n):
	if n == 0:
		return 0
	if n <= 2:
		return 1
	return fib(n-1) + fib(n-2)
# print(fib(0), end=", ")
# print(fib(1), end=", ")
# print(fib(2), end=", ")
# print(fib(3), end=", ")
# print(fib(4), end=", ")
# print(fib(5), end=", ")
# print(fib(6), end=", ")
# print(fib(7), end=", ")
# print(fib(8), end=", ")
# count=[1,2,3,4,5,6,7,8]
for i in range(0,9):
	_list=[]
	_list.append(fib(i))
	print(_list)
	# z=zip(count,_list)
	# print(dict(z))
	# print(",".join(str(_list)))


# lambda 匿名函数：逻辑简单，调用次数少
# 格式 lambda 参数：执行语句
def echo():
	print("helloworld!")
f = lambda : print("helloworld!")
f()
def sxt_sum(a, b):
	return a + b
num = lambda a, b: a + b
print(num(2, 5))


a. 惰性函数(蓄势待发，准备着)，记录上下文环境，多线程会使用
b. yield 关键字实现惰性 -> next(函数引用)
c. 可以返回值
# 函数生成器

# 边玩游戏边学习 5 次
def game():
	for idx in range(1, 6):
		yield print("玩游戏...很开心...")
	return "done"
def study():
	for idx in range(1, 6):
		yield print("helloworld!")
	return "done"
# 可迭代
for i in range(1, 6):
	next(game())
	next(study())
def fib(n):
	a = 0
	b = 1
	for idx in range(0, n+1):
		yield a
		print(a, end=",")
		a, b = b, a+b
sxt_fib = fib(500000000)
for i in range(1, 10):
	next(sxt_fib)


# a. 给偏函数取名 -> import functools functools.partial()
# b. 给定固定的值
import functools
# 偏函数：写一个翻译的小练习
def translate(content, charset):
	# 编码为 utf-8 格式
	if charset == 0:
		return content.encode(encoding="utf-8")
	# 编码为 unicode
	if charset == 1:
		return content.encode(encoding="unicode_escape")
msg = translate("今天天气不错", charset=0)
print(msg.decode("utf-8"))
msg = translate("今天天气不错", charset=1)
print(msg.decode("unicode_escape"))
print("*"*50)
# 给偏函数起名
translate_utf8 = functools.partial(translate, charset=0)
translate_unicode = functools.partial(translate, charset=1)
# 调用偏函数
msg = translate_utf8("今天天气不错")
print(msg.decode("utf-8"))
msg = translate_unicode("今天天气不错")
print(msg.decode("unicode_escape"))
'''

# a. 函数嵌套函数
# b. 返回内函数
# c. 内函数引用外部函数环境
# 闭包实现：浇花
def water_flowers(flowers, ml):
	print("给{}浇水{}ml".format(flowers, ml))
water_flowers("菊花", 50)
water_flowers("梅花", 50)
water_flowers("兰花", 50)
print("*"*50)
# 先装水 -> 外函数装水 内函数使用水浇花
'''
def hold_flowers(ml):
	_list = [ml,]
# 给哪个花浇水
def _flowers(flowers):
	if _list[0] > 0:
		_list[0] = _list[0] - 50
		print(" 给 {} 浇 水 {}ml ， 还 剩 余 {}ml 水 ".format(flowers, 50, _list[0]))
	else:
		print("请装水...")
	return _flowers
'''
def hold_flowers(ml):
	_dict = {"water" : ml}
# 给哪个花浇水
	def _flowers(flowers):
		if _dict["water"] > 0:
			_dict["water"] = _dict["water"] - 50
			print(" 给 {} 浇 水 {}ml ， 还 剩 余 {}ml 水 ".format(flowers, 50,
			_dict["water"]))
		else:
			print("请装水...")
	return _flowers
f = hold_flowers(200)
f("梅花")
f("兰花")
f("菊花")
f("玫瑰花")
f("仙人掌")
