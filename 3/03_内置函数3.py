"""
sorted：排序
"""

lst = [12, 22, 123, 43, 425, 2342, 525]
s = sorted(lst)
print(s)  # 默认是从小到大
s = sorted(lst, reverse=True)  # True代表进行翻转
print(s)


def func(item):
    return len(item)


lst2 = ["住宿费", "学费", "贝吉塔", "卡卡罗特", "xskzhq"]
print(sorted(lst2, key=func))  # sorted会把列表里面的每一项都传递给函数，然后按照函数的返回的长度来进行排序

# 匿名函数:
s2 = sorted(lst2, key=lambda item: len(item))
print(s2)  # 一般的lambda配合sorted来使用

lst3 = [
    {"id": 1, "name": "xsk", "age": 18, "salary": 5200},
    {"id": 2, "name": "xsk11", "age": 181, "salary": 15200},
    {"id": 3, "name": "xsk222", "age": 183, "salary": 52200},
    {"id": 4, "name": "xsk333", "age": 1128, "salary": 523100},
    {"id": 5, "name": "xsk4444", "age": 128, "salary": 52020},
    {"id": 6, "name": "xsk55555", "age": 118, "salary": 520310}
]

# 1.按照每个人的年龄进行排序：
print(sorted(lst3, key=lambda item: item["age"]))

# 2.按工资的大小进行排序，要求从大到小
print(sorted(lst3, key=lambda item: item["salary"], reverse=True))

# 按名字的长度进行排序:
print(sorted(lst3, key=lambda item: len(item["name"]), reverse=True))

"""
filer：筛选
"""

lst = ["住宿费", "学费", "贝吉塔", "卡卡罗特", "xskzhq", "asdf", 'sfdaf', "asfdf"]
f = filter(lambda item: not item.startswith("a"), lst)  # filter返回的是一个生成器
f.__next__()
print(list(f))

"""
map:映射
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [item * item for item in lst]
print(result)

r = map(lambda item: item ** 2, lst)  # 得到的也是一个生成器
print(r)  # <map object at 0x000001A8C270C9D0>
r.__next__()
print(list(r))
