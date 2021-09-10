'''
python先__new__方法开辟空间
继承：子承父业
a. 沿用父类信息
b. 重写父类信息
c. 新增自己信息
格式：
class F(object):
	pass
class C(F):
	pass
'''
# 继承
class Person(object):
	age = 18
	def __new__(cls):
		print("调用父类 Person 开辟空间")
		return object.__new__(cls)
# 重写父类 object 的__init__
	def __init__(self):
		print("调用父类 Person 初始化方法")

class User(Person):
	def __new__(cls, name):
		print("调用 User 自己开辟空间")
		return object.__new__(cls)
# 重写父类 Person 的__init__
	def __init__(self, name):
		print("调用 User 自己的初始化方法")
		self.name = name
u = User('张三')
print(u.age)
Person.sex = 1
print(u.sex)
#就近原则：自己没有找父亲，向上追溯继承链