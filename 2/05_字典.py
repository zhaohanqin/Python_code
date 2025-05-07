# 字典以键值对来存储数据
dic = {"1": 2, '3': 4, '5': 6}
print(dic)
val = dic["1"]  # 索引是键，返回的是值

# 字典的key必须是可哈希的，即不可变的
# 字典的value可以是任何的数据类型

# 字典的增删改查
dic = dict()

# 字典的新增
dic["jay"] = "周杰伦"
dic[1] = 123
print(dic)

dic['jay'] = "昆凌"  # 因为字典里面已经有"jay"了，所以，此时执行的是修改操作
print(dic)

dic.setdefault("tom", "胡辣汤")  # 字典的新增,真实的含义是设置默认值，如果以前有key了，就不起作用了
dic.setdefault("tom", "胡辣")
dic.setdefault("tom", "胡")
print(dic)

# 字典的删除
dic.pop("jay")
# del dic[1]  # 第二种删除的方式
print(dic)

# 查询
print(dic[1])  # 查询到的结果是value，如果key不存在，程序会报错
print(dic.get(1234))  # 如果key不存在，程序返回None

# None
a = None  # 单纯的就是空，表示什么都没有
print(type(a))

# 字典的循环和嵌套
dic = {
    "xsk": 12345,
    "zhq": 1234567,
    "qwe": 12343,
    "wer": 123456
}
for key in dic:
    print(key, dic[key])
# 把字典所有的key保存到一个列表中
print(dic.keys())  # 拿到所有的key
print(list(dic.keys()))  # 保存到列表中
print(dic.values())  # 拿到所有的value
print(list(dic.values()))  # 保存到列表中

# 直接拿到字典里面的key和value
print(dic.items())
print(list(dic.items()))
for item in dic.items():
    key = item[0]
    value = item[1]
    print(key, value)
    print(item)
    print(type(item))  # value的类型是一个元组

# key,value=tuple(key,value),这个过程被称为解包(解构)
for key, value in dic.items():
    print(key, value)

# 练习
dic = {
    "xsk": 12345,
    "zhq": 1234567,
    "qwe": 12343,
    "xer": 123456
}

for key in dic:  # 这种方法会报错，字典循环过程中，不能改变字典的大小
    if key.startswith("x"):
        pass
# dic.pop(key)#dictionary changed size during iteration

# 和列表相同，应该先创建一个列表来存储
temp = []
for key in dic:  # 这种方法会报错，字典循环过程中，不能改变字典的大小
    if key.startswith("x"):
        temp.append(key)
for item in temp:
    dic.pop(item)
print(dic)

dic = {
    ("xsk", 12): 12345,#元组不可哈希
    "zhq": 1234567,
    "qwe": 12343,
    "xer": 123456
}
