"""
for 变量 in 可迭代:
    pass

iterable:可迭代的东西
str,list,tuple,dict,set,open()

可迭代的数据类型都会提供一个迭代器，迭代器可以把数据类型里面的数据一一拿到

获取迭代器的两种方案：
    1.iter()内置函数可以直接拿到迭代器
    2.__ier__() 特殊方法

从迭代器中拿到数据：
    1.next()内置函数
    2.__next__() 特殊方法

总结：迭代器统一了不同数据类型的遍历的作用

迭代器本身也是可迭代的
迭代器的特性：
    只能向前去拿，不能反复
    特别节省内存
    惰性机制
"""

it = iter("你的名字")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))#StopIteration：迭代已经停止了，不能再从里面拿数据了
it = "呵呵哒".__iter__()
print(it.__next__())
print(it.__next__())
print(next(it))

# 迭代器本身可以被迭代
s = "12313414"
it = iter(s)
for mm in it:
    print(mm)
