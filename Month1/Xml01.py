'''
一、理解
标记语言，是一种将文本（ Text）以及文本相关的其他信息结合起来，展现出关
于文档结构和数据处理细节的电脑文字编码。当今广泛使用的标记语言是超文本
标记语言（HyperText Markup Language， HTML）和可扩展标记语言 (Extensible Markup Language XML)。
标记语言广泛应用于网页和网络应用程序。

1、超文本标记语言HTML
a. 写法格式： <a href="link.html">link</a>
b. 关注数据的展示与用户体验
c. 标记是预定义、不可扩展的（如 <a></a>表示超链接）
2、可扩展标记语言XML
a.写法格式：同 html 样式
b.仅关注数据本身
c.标记定义
xml 和 Html 语言由同一种父语言 SGML(Standard Generalized Markup Language, 标准通用标记语言)发展出来的两种语言。
xml 由 html 发展而来，与 html 格式相似，但是比 html 严格。 XML描述的是结构、内容和语义，它不描述页面元素的格式化。
HTML侧重于如何表现信息，内容描述与显示整合为一体。 XML中的每个元素名都是成对出现的。结束标签前加一个/如:<foot></foot>
1、语法规范
a.必须要有XML声明，首行编写
b.必须有且只有一个根元素
c.严格区分大小写
d.属性值用引号(双引号或单引号)，如：属性名="属性值"；在一个元素上，相同的属性只能出现一次
e.标记成对编写
f.空标记关闭，如：</br>
g.元素正确嵌套(格式问题，成对编写)
2、元素命名规则
a. 名称中可以包含字母、数字或者其他可见字符；
b. 名称不能以数字开头；
c. 不能以XML/xml/Xml…开头(关键字)；
d. 名称中不能含空格；
e. 名称中不能含冒号（注：冒号留给命名空间使用）
'''