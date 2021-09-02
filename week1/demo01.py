'''第二天回顾'''
'''
#简单模拟用户登录
username='qiao'
password='123456'
print('欢迎登录！')
count=1#计数器
while count <= 2 :
	username1=input("请输入用户名：")
	password1=input("请输入密码：")
	count+=1
	if username == username1 and password == password1:
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
'''
#容器 list tuple dict set  (键值对里使用了hash算法，可快速查找；set自带去重)
#list操作
list_0=[1,]
list_1=[1,4,3,3,'223',True]
'''
print(list_1[4])
print(list_1[-1])
print(len(list_1))
list_1[3]=list_0
print(list_1)
#print(list_1[6])
a=(1,2,3)
print(type(a))
a_list=list(a)
print(type(a_list))
b_list=list(range(1,4))
print(b_list)
c_list=a_list+b_list
print(c_list*2)
#获取、分片
print(list_1[:])#获取全部
print(list_1[0:])#获取全部
print(list_1[::2])#类似于步长
print(list_1[-1:-5])
print(list_1[-5:-1])
print(list_1[-1:-5:-1])
#list_1[1:3:1]=['aaa']#不匹配就会丢掉
#print(list_1)
#list_1[1:3:1]=['aaa','bbb']#匹配就不丢
#print(list_1)
#list_1[1:3:1]=['aaa','bbb','ccc']#连续追加
#print(list_1)
'''
'''
# 去重
# 第一种：统计去重
sxt_list = ['shsxt', 'sxt', 'sxt', 'shsxt']

for e in sxt_list:
	c = sxt_list.count(e)
	if c > 1:
		sxt_list.remove(e)
print(";".join(sxt_list))#分隔元素
'''

'''
# 第二种：判断去重
sxt_list = ['shsxt', 'sxt', 'sxt', 'shsxt']
sxt_list2 = []

for e in sxt_list:
	if e not in sxt_list2:
		sxt_list.append(e)
	sxt_list = sxt_list2
print(";".join(sxt_list))
'''

'''
# 第三种：set集合去重
sxt_list = ['shsxt', 'sxt', 'sxt', 'shsxt']
sxt_list = set(sxt_list)
print(";".join(sxt_list))
'''

# 常用操作
sxt_list=['shsxt','bjsxt','cssxt','gzsxt','szsxt',False,False,'shsxt']
print("列表长度：", len(sxt_list))
# 增加相关
sxt_list.append("msg") # 追加元素
sxt_list.append([1,2,3]) # 追加新列表
print("追加：", sxt_list)
sxt_list.extend(["A", "B"]) # 将新列表中的元素添加到末尾
print("将新列表中的元素添加到末尾:", sxt_list)
sxt_list.insert(10, "in") # 在某个位置插入元素
print("插入：", sxt_list)
# 删除相关
sxt_list.remove([1, 2, 3]) # 移除元素
print("移除后的元素：", sxt_list)
print("弹出一个元素：", sxt_list.pop())#出栈操作，弹出最后一个元素
print("弹出后列表：", sxt_list)
sxt_list.__delitem__(1) # 删除下标为 1 的元素 __下划线开头和结尾代表特殊方法专用标识 如__init__()代表构造函数
print("删除下标为 1 的元素", sxt_list)
del sxt_list[1] # 根据下标删除元素
sxt_list.clear() # 清空列表
print("清空：", sxt_list)
# 修改相关
sxt_list=['shsxt','bjsxt','cssxt','gzsxt','szsxt',False,False,'shsxt']
sxt_list[1] = "update"
print("修改了 sxt_list 的下标为 1 的元素：", sxt_list)
# 获取相关 [下标]
print("查询某个值所在的下标,找不到报错：", sxt_list.index(False, 0, 8))#str.index(str, beg=0, end=len(string)) str是要找的字符，beg是开始索引，end是结束索引
print("统计某个值在数组中的个数：", sxt_list.count("shsxt"))
print("是否包含 shsxt：", sxt_list.__contains__("shsxt"))#是否包含
for i in sxt_list:
	print("元素：", i) # 遍历
for i in range(0,4):
	print("元素：", sxt_list[i])
for i in sxt_list[0:4]:
	print("元素：", i)
# 其他
sxt_list_new = sxt_list.copy(); # 复制|克隆
print("复制后的 list：", sxt_list_new)
sxt_list.reverse() # 反转
print("将顺序反转：", sxt_list)
num_lists = [7, 6, 8, 9, 2, 3, 1]
num_lists.sort(reverse=False) # reverse 就是排序的顺序为 False 就是按从小到大，True 就是从大到小， 默认是 False
print("排序：", num_lists)