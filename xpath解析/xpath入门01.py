# xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集
"""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>


"""

# /book/price
# xapth解析

from lxml import etree

xlm = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
                <div>
                    <nick>惹了wwww</nick>
                </div>
        </div>
        <div>
            <nick>惹了1213</nick>
        </div>
        <span>
            <nick>112413421</nick>
        </span>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree = etree.XML(xlm)
tree.xpath('/book')  # /表示层级关系，第一个/是根节点
# result=tree.xpath('/book/name')
result = tree.xpath('/book/name/text()')  # text() 拿文本
result2 = tree.xpath('/book/author/nick/text()')  # 可以拿到子节点的文本信息
result3 = tree.xpath('/book/author//nick/text()')  # 可以拿到子节点的文本信息,同时可以拿到子节点的子节点的文字信息
result4 = tree.xpath('/book/author/*/nick/text()')  # *代表任意的节点，通配符
result5 = tree.xpath('/book//nick/text()')  # 拿取所有的nick
result6 = tree.xpath('/book/*/nick/text()')  # 拿取所有子节点的nick
result7 = tree.xpath('/book/*//nick/text()')  # 拿取所有子节点和子子节点的的nick
result8 = tree.xpath('/book/*/*/nick/text()')  # 拿取所有子子节点的的nick

print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
