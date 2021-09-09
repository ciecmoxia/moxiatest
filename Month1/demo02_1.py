#检索会员邮箱
# dict = {'Name': 'Runoob', 'Age': 27}
# print(dict.get('Name'),type(dict.get('Name')))
# print(dict['Age'],type(dict['Age']))
'''
1、域名+会员 —>
2、存储在字典中，相同的域名，用户名放在列表中
3、循环处理，查询
'''
'''
datas='123456@qq.com;654321@qq.com;101010@163.com;666666@sina.com'.split(";")
#print(datas)
users={}
for data in datas:
	#print(data)
	email=data.split("@")
	#print(email)
	uname=email[0]#value，用户
	host=email[1]#key,域名
	#print(uname,host)
	u=users.get(host,[])#获取,这是字典users里是空的,[]是为了不报错，默认返回
	#print(u,type(u))
	# print(users)
	u.append(uname)
	if len(u) != 0:  # 判断字典是否为空，为空则让
		users[host] = u  # 字典里面没有，所以会追加

	if len(u)==0:#判断字典是否为空，为空则让
		u.append(uname)
		users[host]=u#字典里面没有，所以会追加
		# print(users)
		# print(users[host],type(users[host]))
	else:
		u.append(uname)

print(users)
while 1:
	web=input("请输入域名：")
	if web in users:
		print(",".join(users[web]))
	else:
		print("域名不存在！")
	#迭代因子，是否继续检索
	tips=input("是否继续，输入yes继续，输入其他退出：")
	if tips=='yes':
		continue
	else:
		break

#简单模拟用户登录,字典实现
users_dict={'username':'qiao','password':'123456'}
users_dict=dict(username='qiao',password='123456')
print('欢迎登录！')
count=1#计数器
while count <= 2 :
	username1=input("请输入用户名：")
	password1=input("请输入密码：")
	count+=1
	if users_dict['username'] == username1 and users_dict.get("password") == password1:
		print("*"*15)
		print('*'*3,'登陆成功','*'*3)
		print("*"*15)
		break
	else:
		print("用户名或密码错误，请重新输入，您还有%d次机会！"%(3-count))
		t=3-count
	if t == 0:
		print('没几乎喽！')
		break

#set集合{}
# set_0=set([1,4,3,[3],'22',(3,True)])无法去重，[3]为可变对象,set函数只能传一个参
set_0=set(['22',(3,True)])
print(set_0,type(set_0))
set_1=(1,4,3,[3],'22',(3,True))
print(set_1,type(set_1))#这是元组tuple
set_2=set({'Name': 'Run', 'Age': 27,'Age':21})#会自动丢弃value值
print(set_2,type(set_2))
# 数学操作
sxt_set = {1,2,3,4,3} & {1,2,7,8,5} # 交集 set1.intersection(set2)
print(sxt_set)
sxt_set = {1,2,3,4,3} | {1,2,7,8,5} # 并集 set1.union(set2)
print(sxt_set)
sxt_set = {1,2,3,4,3} - {1,2,7,8,5} # 差集 set1.difference(set2)
print(sxt_set)
sxt_set = {1,2,3,4,3} ^ {1,2,7,8,5} # 对称差集
print(set_0.symmetric_difference(set_2))#也是对称差
print(sxt_set)

# 常用方法
fruits = {'apple', 'orange', 'pear', 'tomato', 'cucumber'} #增加 相关
fruits.add("banana")
print("添加香蕉：", fruits)
#删除 相关
fruits.remove('apple') # 如果移除的元素不在集合中就会报错
print("移除 apple 后：", fruits)
fruits.discard("pear") # 跟 remove()的区别就是移除的元素可以不在集合中
print("移除元素后：", fruits)
# 随机弹出一个元素
random_fruit = fruits.pop()
print("随机弹出一个元素：", random_fruit)
print("fruits 是否包含 apple", fruits.__contains__('apple'))
new_fruits = fruits.copy()
print("复制一个集合：", new_fruits)
# 清空元素
fruits.clear()
print("清空元素后：", fruits)
# 包装成定长集合，没有了 add remove 方法
s = frozenset(('a', 'a', 'b', 'c', 'd', 1, 2.8, False))
s.add('f') # 报错
'''