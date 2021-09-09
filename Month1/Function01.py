import random #->使用 x = random.randint(a,b)
from random import randint#->使用 x = randint(a,b)
from random import * #->使用 x = randint(a,b)
# from (自己写的.py) import (函数)
# import (自己写的.py)
'''
a,b=0,1
for i in range(0,6):
	if i==5:
		print(a)
	else:
		print(a, end=",")
	a,b=b,a+b

num1 = random.randint(1,5)
num2 = randint(1,5)
print(num1, num2) # 导入 copy 模块

from copy import deepcopy
import copy
a = (1,2)
b = copy.deepcopy(a)
c = deepcopy(a)
print(a, b, c)
'''
'''
# 认识函数
from my_def01 import * # 导入 my_def01 模块下的所有函数 -> 可以直接使用函数-> sxt_range(min, max) | sxt_abs(num)
import my_def01 # 导入 my_def01 模块下的所有函数 -> 需要 模块.函数 使用 ->
my_def01.sxt_range(min, max) | my_def01.sxt_abs(num)
# 使用函数
a = my_def01.sxt_abs(-5) b = sxt_abs(-5)
print(a, b) # 使用函数
a = my_def01.sxt_range(1, 6) b = sxt_range(1, 6)
print(a, b)
'''

# 1)、函数名为 print_hello,实现输出"hello world"的函数
def print_hello():
	print("hello world...")
# 2)、函数名为 print_5,实现输出 5 的功能的函数
def print_5():
	print(5)
# 3)、函数名为 sum_12,实现输出 1+2 的和的函数
def sum_12():
	print(1+2)
# 4)、函数名为 print_fib6,实现打印 0,1,1,2,3,5
def print_fib6():
	a = 0
	b = 1
	for idx in range(0, 5+1):
		print(a, end=",")
		a, b = b, a+b
print_hello()
print_5()
sum_12()
print_fib6()

# 1)、函数名为 print_msg,实现输出 msg 的函数
def print_msg(msg):
	print(msg)
# 2)、函数名为 print_num,实现输出正数的功能的函数
def print_num(num):
	if isinstance(num, int) and num > 0:
		print(num)
# 3)、函数名为 sum_ab,实现输出两个数的和的函数
def print_ab(a,b):
	print(a+b)
# 4)、函数名为 print_fib,实现打印前 n 个斐波那契数列
def print_fib(n):
	a ,b =0, 1
	for idx in range(0, n+1):
		print(a, end=",")
		a, b = b, a+b
# 函数调用
tips = input("请输入一句话:")
print_msg(tips)
print_num(1)
print_num(-1)
print_num("字符串")
i, j = 1, 2
print_ab(j,i)
print_fib(10)

a=abs
'''
box=a(-5)
print(box)
'''
print(a(-5))#节省空间