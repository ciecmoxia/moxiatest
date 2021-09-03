'''
# 使用字面值
sxt_int = (1)
print(type(sxt_int))
sxt_tuple = (1,) # 推荐使用这种
print(type(sxt_tuple))
sxt_tuple = (1, 2, 3, 'sxt', 'is', 'very', 'good', True)
# 使用构造函数
sxt_tuple = tuple([1, 2, 3, 'sxt', 'is', 'very', 'good', True]) # 将列表转为元组
sxt_tuple = tuple(range(1, 11, 2)) # 获取奇数
sxt_tuple = tuple(range(2, 11, 2)) # 获取偶数
# 脚本操作符
sxt_tuple = (1, 2, 3) + (3, 2, 1) # 合并为一个容器
sxt_tuple = (1, 2, 3) * 5 # 重复多次
# 获取
sxt_tuple = (1, 2, 3, 'sxt', 'is', 'very', 'good', True)
print(sxt_tuple[0])
print(sxt_tuple[-8])
print(sxt_tuple[len(sxt_tuple)-5])
# print(sxt_tuple[15]) # 越界
# 长度
print(len(sxt_tuple))
# 不可改变
# sxt_tuple[3] = 'shsxt'
# print(sxt_tuple)#tuple不可变元素
# 分片 左闭(包含)右开(不包含)
sxt_tuple = (1, 2, 3, 'sxt', 'is', 'very', 'good', True)
print(sxt_tuple[1:5]) # 指定索引(2, 3, 'sxt', 'is')
print(sxt_tuple[:]) # 所有
print(sxt_tuple[0:]) # 所有
print(sxt_tuple[0::2]) # 偶数索引(1, 3, 'is', 'good')
print(sxt_tuple[-1:-5:-1]) # 指定索引倒序获取(True, 'good', 'very', 'is')
print(sxt_tuple[-2:4]) #[] 倒序可以获取到数据正序是空
'''
'''
#dict
dict_0={'name':'qiao','pw':123,'sex':['男']}
dict_1={'a':1,'b':2,}
print(dict_1,type(dict_1))
dict_2=dict([('q',1),('w',2),('e',3)])
dict_3=dict((('q',1),('w',2),('e',3)))
dict_4=dict((['q',1],['w',2],['e',3]))
dict_5=dict(q=1,w=2,e=3)
print(dict_2,dict_3,dict_4,dict_5)
'''
'''
# 常用方法
sxt_dict = {'name':'老王', 'sex':1, 'address':'隔壁', 'address':'松江'} # 增加相关
sxt_dict['no'] = 10#有就更改，没有增加
print(sxt_dict)

sxt_dict = {}.fromkeys(['a','b','c'], [1,2,3])
print(sxt_dict)
sxt_dict = {}.fromkeys(['a','b','c'], None)
print(sxt_dict)
sxt_dict = {}.fromkeys(['a','b','c'], 1)
print(sxt_dict)

# 删除相关
del sxt_dict['no'] # 如果没有键 no 会出现异常
print(sxt_dict)
sxt_dict.pop('sex') # 成功返回 1 如果没有 key，默认错误
print(sxt_dict)
sxt_dict.pop('sex',-1) # 避免错误，返回-1，这里已经删除
print(sxt_dict)
sxt_dict.popitem() # 随机删除 item
print(sxt_dict)

# 更改相关
sxt_dict['name'] = 'laopei' # 存在则覆盖，不存在新建
print("修改后的名称：", sxt_dict['name'])
sxt_dict.__setitem__('name', 'shsxt')
print("修改后的名称：", sxt_dict['name'])

sxt_dict ={'name':'老王', 'sex':1, 'address':'隔壁', 'address':'松江'}
sxt_dict.update({1:'a', 'name':'b', 3:'c'}) #所有键-值对添加到当前字典中，并覆盖同名键的值, 有的则覆盖，没有的添加 print(sxt_dict)
print(sxt_dict)

# 查询相关
sxt_dict ={'name':'老王', 'sex':1, 'address':'隔壁', 'address':'松江'}
print('name' in sxt_dict) #使用 in 查找是否存在
print(sxt_dict['name1'] if 'name1' in sxt_dict else 'notexists' ) #使用三目运算符，true返回左边，没有就返回右边
print(sxt_dict['name'] if 'name' in sxt_dict else 'sorry')
print("姓名：", sxt_dict['name']) # [key] 没有 key 会出异常
print("姓名：", sxt_dict.get('name')) #没有 key 返回""
print("姓名：", sxt_dict.get('gender', 'boy')) #没有 key 返回"boy"
# 获取所有的 key 值和 value 值,返回的是一个 set 集合
print("所有的 key 值：", sxt_dict.keys())
print("所有的 values 值：", sxt_dict.values())
# 循环遍历获取所有的内容
for k, v in sxt_dict.items():
	print("key 值：", k, "，value 值：", v)#k,v只是变量名，随意
'''
#统计单词次数
'''
1、输入短句，统计单词
2、分割字符串，声明字典
3、循环处理、查询
Talk is cheap,show me your code,show me your code!
'''
msg=input("请输入一段英语短句：")
msg_list=msg.split()#默认空格分割，形成列表
print(msg_list)
dict_count={}
for m in msg_list:
	if m not in dict_count:
		dict_count[m]=1
	else:
		dict_count[m]=dict_count[m]+1
print(dict_count)
# #查询
# select_word=input("请输入想要查询的单词：")
# print("{}该单词出现的次数是：{}".format(select_word,dict_count.get(select_word,0)))
#循环获取
for letter,count in dict_count.items():
	print(letter,count)
for count in dict_count.values():
	print(count)
