'''
封装、继承、多态
面向过程——>单一流水线，linux内核、git内核等，牵一发而动全身
面向对象——>用类造对象，上帝过程，万物皆可对象.属性、方法

属性：类属性、对象属性
方法：类方法（@classmethod def xxx()...）、对象方法（self），静态方法(@staticmethod)
	a. 对象.拷贝的类属性，如果赋值，新开辟空间，否则指向原有的类的属性空间
	b. 对象追加的属性属于对象自己，类加入的属性，属于所有对象

self  实例方法、对象方法 -> 属于对象本身的方法
格式：def 方法名(self):
		方法体
cls -> @classmethod
		类方法
格式：@classmethod
	 def 方法名(cls):
	 	方法体
2.3、静态方法 -> @staticmethod与对象和类无关
格式：@staticmethod
	 def 方法名():
	 	方法体
'''

# 定义天使类：属性、方法
class Angel: # 大驼峰
	# 属性
	kind = True
	wing = "1 对"
	gender = 0 # 方法
	def help(self):
		print("拯救学习 java 和 python 的码农们")
	def fly(self):
		print("忽隐忽现")

'''
# 定义天使类：属性、方法
class Angel(object): # 大驼峰
	# 属性
	kind = True
	wing = "1 对"
	gender = 0 # 方法
	def help(self):
		print("拯救学习 java 和 python 的码农们")
	def fly(self):
		print("忽隐忽现")

def main():
	print(type(Angel))
	print(dir(Angel))
if __name__ == '__main__':
    main()
'''
'''
# print(type(Angel))
# print(dir(Angel))
a=Angel()
print(type(a.__class__))
print(a.gender)
a.age=18#对象属性
print(a.__dict__)
print(Angel.__dict__)


# 定义杯子：属性、方法
class Cup3(object):
	# 类属性
	ml = 100

	def __init__(self, color, mat):  # 定制方法，初始化方法，对象被构建就会被执行，为了方便
		# print(id(self))
		self.color = color
		self.mat = mat

	# 对象方法、实例方法
	def show_info(self):
		print(self.color + "-->" + self.mat + "杯子")


c = Cup3("黑色", "玻璃")
c1 = Cup3("白色", "塑料")
c.show_info()
c1.show_info()
print(c.__dict__)
print(dir(c))
# Cup3.show_info()
print(dir(Cup3))


# 定义人类：属性、方法
class Person(object):
	# 类的属性
	name = "老王"
	age = 18

	# 实例方法
	def smile(self):
		print("奸笑中....")


# 实例化对象
p = Person()
print(p.name + "-->" + str(p.age))  # 指向类的属性
p.name = "老裴"  # 对象的属性
print(p.name + "-->" + str(p.age))
p1 = Person()  # 指向类的属性
print(p1.name + "-->" + str(p1.age))

Person.name = "老马"  # 类的属性
Person.age = 46
# 对象名.拷贝的类属性 如果赋值，新开辟空间，否则指向的 原有的类的属性空间
print(p1.name + "-->" + str(p1.age))
print(p.name + "-->" + str(p.age))  # 更改了，拥有自己的空间

# 随意的加入
p.gender = '你懂得'
# print(p1.gender)  # 'Person' object has no attribute 'gender'
Person.gender = '女'  # 属性必须一样
print(p1.gender)
print(p.gender)
'''
class Dog:
	name='cool'
	color='yellow'
	age=2

	#构造方法、初始化
	def __init__(self,eat):
		self.eat=eat
		print('{}爱吃的是：{}'.format(self.name,eat))

	#对象方法、实例方法
	def show_info(self):
		print('对象方法、实例方法:'+'My dog is named %s,its color is %s,its age is %d'%(self.name,self.color,self.age))

	#类方法
	@classmethod
	def show_info2(cls):
		print('类方法:' + 'My dog is named %s,its color is %s,its age is %d' % (cls.name, cls.color, cls.age))

	#静态方法
	@staticmethod
	def show_info3():
		print('静态方法:' + 'My dog is named 123,its color is 321,its age is 1' )

d1=Dog('meat')
d2=Dog('hotdog')
d1.show_info()
d1.show_info2()
d1.show_info3()
#Dog.show_info()#python不支持对象方法，必须传参，python提供了类方法可以使用
Dog.show_info2()
Dog.show_info3()
Dog.like='玩皮球'
print(d1.like)
print(id(Dog.color))
Dog.color='white'#重新赋值，一样不会开辟新空间，不一样会开辟新空间
print(id(Dog.color))
Dog.color='yellow'
print(id(Dog.color))
print(d1.eat)#self.eat=eat这步操作的原因

# def show(d1):
# 	print('My dog is named %s,its color is %s,its age is %d'%(d1.name,d1.color,d1.age))
# show(d2)

import sys

__author__ = '大名'


# 构建人类
class Person(object):
	sex = True  # 类属性

	# 初始化对象属性
	def __init__(self, name, age):
		self.name = name
		self.age = age

	__slots__ = ("name", "age",)


# 对类无效
Person.sex = False  # 修改
print(Person.sex)

# 对对象有效
p = Person("张三", 18)
# p.sex = True # 不可以新增
# p.sex = False # 不可以修改 只读
print(p.sex)

import sys

__author__ = '大名'


# 构建杯子类
class Cup(object):

	# 初始化对象属性
	def __init__(self, color, mat):
		self.color = color
		self.mat = mat

	def __str__(self):
		return "{}-->{}".format(self.color, self.mat)

	def __repr__(self):
		return "{s.color}-->{s.mat}".format(s=self)


c = Cup("白色", "玻璃")
print(c)
print(Cup("黑色", "塑料"))
print(c.__str__)
print(Cup.__repr__)
print(str(c))
print(repr(c))

