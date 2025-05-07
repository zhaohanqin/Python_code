from lxml import etree

tree = etree.parse("b.html")
tree.xpath('/html')
result1 = tree.xpath('/html/body/ul/li/a/text()')#拿到浏览器的名称
result2 = tree.xpath('/html/body/ul/li[1]/a/text()')#拿到百度的名称，[]表示索引

print(result1)
print(result2)


print("------------------------------------")

result3=tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')#[@xxx=xxx] 属性的筛选
print(result3)

ol_li_list=tree.xpath('/html/body/ol/li')
for li in ol_li_list:
    # print(li)
    #提取对应的文字
    print(li.xpath('./a/text()'))#这里的./代表的是相对查找，相对于li来进行查找
    result4=li.xpath('./a/@href')#直接拿到属性的值
    print(result4)

print("------------------------------------")
print(tree.xpath('/html/body/ul/li/a/@href'))


print(tree.xpath('/html/body/div[1]'))
'/html/body/div[2]/div[2]/div[1]/div[5]/div/div[4]/div/a'
'//*[@id="mirror-vdcon"]/div[1]/div[5]/div/div[4]/div/a'