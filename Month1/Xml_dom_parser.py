import xml.dom.minidom
# 将获取的xml文档整合成树
dom_tree=xml.dom.minidom.parse('Xml_practice5.xml')
# 获取根节点，应该是全部节点，树里面的所有节点都可以获取
root=dom_tree.documentElement

# 获取xxx子节点
sitcom=root.getElementsByTagName('sitcom')

# test = root.getElementsByTagName('player')
# print(test)

for s in sitcom:
	title=s.getElementsByTagName('title')[0]# 返回的是nodelist，用索引获取
	# print(s.getElementsByTagName('title'))
	print("电视剧名称：",title.childNodes[0].data)#获取节点内容
	print("电视剧导演：",title.getAttribute('director'))#获取属性内容
	players=s.getElementsByTagName('players')[0]
	# print(s.getElementsByTagName('players'))
	# print(s.getElementsByTagName('players')[0].childNodes)[<DOM Text node "'\n         '">, <DOM Element: player at 0x1fd4452ae50>,...
	for p in players.childNodes:
		# 只处理元素节点
		if isinstance(p,xml.dom.minidom.Element):
			print('演员名字：',p.childNodes[0].data)
		# print(p)

	desc=s.getElementsByTagName('desc')
	if desc:
		print(desc[0].childNodes[1].data)