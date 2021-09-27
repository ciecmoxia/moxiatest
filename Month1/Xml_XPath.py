import urllib.request as request
from lxml import etree
# xpath只能爬取静态网页

# 模拟浏览器访问地址，并且接受返回的数据
re = request.urlopen('https://www.trustie.net/')

# 将字节数据转化成字符串(整个页面的内容)
html_content = str(re.read(), encoding='utf-8')
# print(html_content)

# 根据字符串获取xml树
tree = etree.HTML(html_content)
# print(tree)

# 获取页面上id为normalthread_开头的节点信息
# results = tree.xpath('//*[@id="normalthread_5989"]/tr/th/a[1]')
results = tree.xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]')
# print(results)

for item in results:
	# print(item)
	try:
		first = item.xpath('./p/text()')[0]
		print(first)
		second = item.xpath('./p[@class="homeDesc"]/text()')
		# print(second)
		second1 = "".join(second)
		print(second1)

		print(second1.replace(' ','').replace('\n', '').replace('\r', ''))
		# _i = item.xpath('./div[@class="foruminfo"]/i[@class="z"]')
		# _text = _i.xpath('./a/span/text()')[0]
		# print(_text)
	except Exception as e:
		print('解析页面元素错误，错误信息为：', e)
