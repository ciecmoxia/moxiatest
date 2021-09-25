import xml.dom.minidom
# a.在内存中创建一个空的文档：doc = xml.dom.minidom.Document()
doc=xml.dom.minidom.Document()
# b.创建一个根节点：root = doc.createElement('节点名')
root=doc.createElement('people')
# 设置根节点的属性
root.setAttribute('id','people')
# c.将根节点添加到文档对象中：doc.appendChild(root)
doc.appendChild(root)
# d.创建根节点的子节点并添加到根节点：root.appendChild(子节点)
# 创建数据
data=[{'name':'熊大','age':12},{'name':'熊二','age':11}]
# 循环创建子节点和属性节点
for i in data:
	#创建节点
	node_person=doc.createElement('peoson')
	# 添加属性
	node_person.setAttribute('name',i['name'])
	node_person.setAttribute('age',str(i['age']))

	#将子节点添加至根节点
	root.appendChild(node_person)
#  e.写 出xml文档：
# doc.writexml(文件, indent="\n", addindent="\t", encoding='utf-8')
with open('Xml_practice4.xml','w',encoding='utf-8') as f:
	doc.writexml(f,indent="\n",addindent="\t",encoding='utf-8')
# tips: 所有的节点创建都是文档创建，所有的节点添加都是appendChild()
