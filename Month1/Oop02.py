#对象构建
'''
1、 开辟空间
类方法：def __new__(cls):new要和init参数一致
# 返回引用
return object.__new__(cls)
2、 初始化属性
实例方法：def __init__(self, 形参|形参列表):
# 绑定属性
self.属性 = 属性
3、 返回引用
注意：
a. 每个对象创建时，__new__ __init__都会被执行且执行一次
b. __new__ __init__两个方法的参数要一致
c. __new__是类方法__init__是实例方法
'''
'''
# 构建商品类
class Goods(object):
	# 类属性
	count = 0 # 开辟空间
	def __new__(cls, name, num, price):
		print("开辟空间，准备创建对象")
		print(id(Goods))
		print(id(cls))
		cls.count += 1  # 返回引用
		return object.__new__(cls)  # 初始化对象信息

	def __init__(self, name, num, price):
		print("初始化对象信息")  # 绑定信息
		self.name = name
		self.num = num
		self.price = price
g = Goods("咖啡", 2, 20)
print(g.name)
g1 = Goods("饼干", 5, 100)
g2 = Goods("饮料", 2, 20)
print(Goods.count)
g3 = g  # 引用的过程 不是构建
print(Goods.count)

# import sys
# sys.getrefcount(s)
# 返回对象引用个数，返回的值 N+1 个
import sys
class Student(object):
	def __init__(self, name):
		self.name = name
	def __del__(self):
		print("我被释放了！")
s = Student('张三')
s1 = s
s2 = s
s3 = s
print(sys.getrefcount(s))

# 构建杯子类
class Cup(object):
	# 初始化对象属性
	def __init__(self, color, mat):
		self.color = color
		self.mat = mat
	def __str__(self):
		return "{}-->{}".format(self.color, self.mat)

	def __repr__(self):
		return "{s.color}-->{s.mat}".format(s=self)#!!!

c = Cup("白色", "玻璃")
print(c)
print(Cup("黑色", "塑料"))
print(c.__str__)
print(Cup.__repr__)
'''
'''
__slots__ = (属性序列,)
a. 内部其实就是干掉了__dict__
b. 对类无效，对对象有效

# 构建人类
class Person(object):
	sex = True # 类属性
	# 初始化对象属性
	def __init__(self, name, age):
		self.name = name
		self.age = age
	__slots__ = ("name", "age",)#我的理解对于对象，只能修改对象的绑定属性，无法修改其他类属性
# 对类无效
Person.sex = False # 修改
print(Person.sex)
# 对对象有效
p = Person("张三", 18)
# p.sex = True # 不可以新增
# p.sex = False # 不可以修改 只读
p.name='李四'
print(p.name)
print(p.sex)


class Student(object):
	score=12
	# def __init__(self, name, age):
	# 	self.name = name
	# 	self.age = age

	__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'

#print(s.__dict__)
print(s.name,s.age)
try:
    s.score = 99#'Student' object attribute 'score' is read-only
except AttributeError as e:
    print('AttributeError:', e)#AttributeError: 'Student' object has no attribute 'score'

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
'''

import types
# 实例方法
def self_method(self):
	print("self_method")
# 类方法
@classmethod
def class_method(cls):
	print("class_method")
# 静态方法
@staticmethod
def static_method():
	print("static_method")
p_field = {'name':'张三', 'age':18}
# type("类名称", (父类列表,), 属性字典(类属性))
Person = type("Person", (object,), p_field)
p = Person()
print(p.name)
print(Person.age)
# 类 -> 绑定实例方法
#Person.self_method = self_method
#Person.self_method(p)
#p.self_method()
# 对象 -> 绑定实例方法
p.self_method = types.MethodType(self_method, p)
p.self_method()
# 只可以类 -> 绑定类方法
Person.class_method = class_method
Person.class_method()
p.class_method()
# 只可以类 -> 绑定静态方法
Person.static_method = static_method
Person.static_method()
p.static_method()