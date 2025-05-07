# set集合，不能有重复的元素
s = {}  # 可变,这样子会被认为是字典
s2 = set()
print(type(s))  # 集合默认是无序的
s = {1, "呵呵", 3, 100, 5}
print(s)

# 不可哈希：python进行数据存储的时候，要进行哈希计算，数据类型应该要可哈希
# 可哈希：不可变的数据类型，int str,tuple,bool
# 不可哈希：list,dict,set


s = set()  # 创建空集合
t = tuple()  # 创建空元组
s1 = str()  # 创建空字符串
l1 = list()  # 创建空列表

s.add("赵本山")
s.add("赵本山")
s.add("赵本4")
s.add("赵本5")
s.add("赵本山")
s.add("范围")
s.add("范伟")
print(s)  # 集合里面不允许有重复的元素

# s.pop()#由于集合无序，不知道丢掉的是谁
s.remove("范伟")
# 想修改，只有先删除，再添加：
s.remove("范围")
s.add("升腾")
print(s)

# 查询
for item in s:
    print(item)

# 交集，并集，差集
s1 = {"刘能", "赵本山", "赵四", '笑了之'}
s2 = {"刘能", "赵本山", "赵四", '刘科长', '肖科长'}
print(s1 & s2)  # 求交集
print(s1.intersection(s2))  # 求交集

print(s1 | s2)  # 并集
print(s1.union(s2))  # 并集

print(s1 - s2)  # 差集
print(s1.difference(s2))  # 差集

# 集合可以去除重复
lst = ["周杰伦", "昆凌", "蔡依林", "侯佩岑", "周杰伦", "昆凌", "蔡依林", "侯佩岑", "周杰伦", "昆凌"]
print(lst)
print(set(lst))
print(list(set(lst)))  # 去除重复之后的数据是无序的
print(lst[1])
