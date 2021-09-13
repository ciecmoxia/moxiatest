'''
a. 字符序列，多个字符
b. 不可变字符序列
c. 字符串与字节串
字符串：人类的语言
字节串：计算机的语言
d. 编码与解码
编码：字符串到字节串
解码：字节串到字符串
e. 字符集
ascii、gbk gbk2312、unicode(其中一种 utf-8)
f. 变量名不要叫 str
'''
# 构建字符串
# 1. '' ""
# 2. '''''' """"""：可以保留格式
# 3. \：可以换行继续编写后续字符串，等同在同一行，没有换行格式
# -*- coding:utf-8 -*-
msg = '十年后的你\
会感谢现在努力奋斗的你！'
print(msg)
msg = '十年后的你'\
	  '会感谢''现在努力奋斗的你！'
print(msg)
msg = "十年后的你\
会感谢现在努力奋斗的你！"
print(msg)
msg = '''十年后的你
会感谢现在 努力奋斗的你！'''
print(msg)
msg = """十年后的你
会感谢现在努力奋斗的 你！"""
print(msg)

# -*- coding:utf-8 -*-
# 转义字符：改变了原有字母的含义，表示特殊意义 \+单个字母
# s = "I'm Mr T"
# 使用''或""特性
s = "I'm Mr T"
# 使用转换字符
s = 'I\'m Mr T'
print("福大命大\\福州大学和闽江大学")
print("剑桥\t 剑南春桥梁建筑学院")
print("西施院\0 西南师范学院")
print("西施院\s 西南师范学院")
print("同居大学\012 同济大学")
print("国务院\x0a 国际商务学院")
print("相思院\n 湘潭师范学院")
print("哈佛\b 哈尔滨佛教学院")
print("北大\r 西北大学")
print("北大\r 西")
print("北大\r\n 西北大学")
print("交际院\r 交通职业技术学院")
# 使用原始字符 r 结束符避免\ 或者手动解决\\转义
msg = r'c:\now'
print(R'武汉大学\\男同学\n 武大郎')
# print(r'D:\Dylan\myPython\day08-字符串\代码\day08\') # 会报错，\的问题
print(r'D:\Dylan\myPython\day08-字符串\代码\day08\\')

# -*- coding:utf-8 -*-
# 运算符
msg = '不要和我比懒' + '我懒得和你比' # 拼接使用 + 字符串与字符串
# msg = '不要和我比懒' + 1 # 必须手动转字符串
msg = '不要和我比懒' + str(1)
msg = '帅有什么用!到头来还不是被卒吃掉？' * 3
msg = '诸葛亮出山前也没带过兵啊，你们凭啥要我有工作经验！！！'
print(msg[0])
print(msg[:]) # 切片 获取一部分
msg2 = msg[:] # 相同的地址 ，指向同一个东西
msg2 = msg[0:]
msg2 = msg[:len(msg)]
print(id(msg))

print(id(msg2))
# 成员运算符 in not in
print('头' in msg)
print('头' not in msg)
for e in msg :
	print(e,end='#')
# help(print)
print()
print('a', 'b', 'c', sep = '#', end = "-->")

# -*- coding:utf-8 -*-
# 字符串格式化 +格式字符串
name= '李彦宏'
age = 50
sql = "SELECT * FROM USER WHERE NAME = '" + name + "' AND AGE = " + str(age)
print(sql)

# -*- coding:utf-8 -*-
# 字符串格式化 %占位格式化
''' 占位符 替换内容
%d 十进制整数
%i 整数
%u 无符号整数
%o 八进制整数
%x %X 十六进制整数
%g G 浮点数取整
%f e E 浮点数 .5f .2f
%s 字符串
%c 字符
%x 十六进制整数
%r 原始字符串
%% %
'''
name, age = '吴恩达', 42
sql = "SELECT * FROM USER WHERE NAME = '%s' AND AGE = %d"%(name, age)
print(sql)
sql = ("SELECT * FROM USER WHERE NAME = {!r} AND AGE = {}").format(name,age)
print(sql)
info = '姓名：%s, 年龄：%s, 身价%d 亿人民币' % ('贝佐斯亚马逊', 54, 7750)
print(info)
print('银行余额%g,加油'%(123.000123)) # 小数部分非 0 保留 3 位 从非 0 开始截取
print('银行余额%f,加油'%(123.000123)) # 输出浮点数
print('银行余额%.2f,加油'%(123.000123)) # 保留两位小数 四舍五入
print('银行余额%5g,加油'%(123.000123)) # 默认右对齐
# print('银行余额%+5d,加油'%(123.000123)) # 默认右对齐 +无效
print('银行余额%-5g,加油'%(123.000123)) # -右对齐
male, female = 7.1137, 6.7871
news = '男：%.1f%%，女：%.1f%% (该数据统计于 2017 年底) 中国男性数量：%.4f 亿人，中国女性数量：%.4f 亿人，男性比女性仍多 3266 万人。' % ((male * 100)/(male + female),
(female*100)/(male + female), male, female) # 保留原始 %r 在控制台演示
news = '消息为:%r-->'%('aaa\nbbb')
news = '消息为:%s-->'%('aaa\nbbb')
# -*- coding:utf-8 -*-
# 字符串格式化 format
''' 格式 说明
{} 字符串形式
{索引} 按位置
{name} 按名称
{集合位置[索引]} 操作集合的元素
{:b}{:d}{:o}{:x}{:.3f} 不同进制的整数、浮点数
{:,} 千分位 1,234,567,890
{:>8} ^、<、>分别是居中、左对齐、右对齐，后面带宽度和一个填充字符，默认按空格
填充
{!r}{!s} 有引号及保留转义和没有引号及转义
'''
print("有引号: {!r}; 没有引号: {!s}".format('test1', 'test2'))
print("有引号: {!r}; 没有引号: {!s}".format('te\nst1', 'te\nst2'))
print('{},{}'.format('laopei', 18)) # 可以不指定索引
print('{0}'.format('laopei', 18)) # 可以使用索引
print('{0},{1},{0}'.format('laopei', 18)) # 可以使用多次
print('{name},{num}'.format(num=100, name='shsxt')) # 使用名称
print("{:<8}".format(211)) # 默认空格填充，8 位，靠左
print("{:#^8}".format(211)) # 8 位，指定#填充,居中
print("{:p>8}".format(211)) # 默认空格填充，8 位，靠右
print('{:,}'.format(123123)) # ,千分位
print('{:.2f}'.format(123123.7698)) # 保留 2 位小数
print('{:,.2f}'.format(123123.7698))
print(' int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(47))
# 进制
print('{0[0]},{0[1]}'.format(['shsxt', 18])) # 访问列表的元素
class Book:
	def __init__(self, name, price):
		self.name, self.price = name, price

	def __str__(self):
		return '书名是:{s.name},价格为:{s.price}'.format(s=self)  # 访问

#属性
print(str(Book('python 入门', 88)))

'''
api
1. count(sub[,start[,end]]) 统计次数
2. find(sub[,start[,end]]) 查找第一次出现的位置，不存在返回-1
index(sub[,start[,end]]) 类似 find()，不同在于如果 sub 不在字符串中，返回的
不是-1 而是异常
3. parititon() 分割，永远返回三个值，如果没有，返回两个空串及源串，保留
split() 分割，可能多个，不保留切割符
splitlines() 按行分割(\n \r\n)
4、strip ([chars]) 去除空格
5、join(iterable) 加入到字符串或可迭代的对象中,要求元素为字符串
6、replace(old, new[, count]) 用指定字符串替换新串，如果没有指定替换次数就是
替换所有
7、upper()、lower() 英文
8、startswith (prefix[, start[, end]]) 是否以某某开头
endswith(sub[,start[,end]]) 是否以某某结尾
9、encode(encoding='utf-8',errors='strict') 编码
decode(encoding='utf-8',errors='strict') 解码
'''