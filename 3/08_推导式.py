"""
推导式：
    简化代码。
    语法：
        列表推导式：[数据 for循环 if判断]
        集合推导式：{数据 for循环 if判断}
        字典推导式：{Key:Vaule for循环 if判断}

    (数据 for循环 if判断)->不是元组推导式，根本就没有元组推导式，这个叫做生成器表达式
"""

lst = []
for i in range(10):
    lst.append(i)
print(lst)

lst1 = [i for i in range(10)]
print(lst1)

# 创建一个列表[1,3,5,7,9]
lst2 = [i for i in range(1, 10, 2)]
lst3 = [i for i in range(10) if i % 2 != 0]
print(lst3)
print(lst2)

# 50件衣服
lst = [f"衣服{i}" for i in range(1, 50)]
print(lst)

# 集合推导式
s = {i for i in range(10)}
print(s)

# 将下列列表修改为字典，要求索引为key，数据作为value
lst = ["hzq", 'qhz', 'zhq', 'ksx', 'sxk', 'xsk']
dic = {i: lst[i] for i in range(len(lst))}
print(dic)
