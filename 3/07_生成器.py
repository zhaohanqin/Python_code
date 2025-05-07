"""
生成器的本身就是迭代器

创建生成器的两种方案：
    1.生成器函数
    2.生成器表达式

生成器函数
    生成器函数中有一个关键字yield
    生成器函数再执行的时候得到是一个生成器，并不会去执行函数

    yield:只要函数中有yield，这就是一个生成器函数
    作用：
        1.返回数据
        2.可以分段的执行函数中的内容,通过__next__()可以执行到下一个yield的位置
        3.可以截断函数
"""


def func():
    print(1234556789)
    yield 999  # yield也有返回的作用，但是只有在函数被__next__()的时候，才会返回数据


ret = func()
ret.__next__()


# print(ret.__next__())  # StopIteration,和迭代器一样的错误


def func2():
    print(123)
    yield 666
    print(456)
    yield 999


ret = func2()
print(next(ret))
print(next(ret))  # 通过__next__()可以执行到下一个yield的位置


# 去工厂定制10000件衣服
def order():  # 直接拿到一万件衣服，对内存的要去很大
    lst = []
    for i in range(1, 10001):
        lst.append(f"衣服{i}")
    return lst


lst = order()


# print(lst)

def order2():  # 分批次拿，每次拿50件
    lst = []
    for i in range(1, 10001):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst
            lst = []  # 清空列表，装下一次的50件衣服即可


ret = order2()
print(ret.__next__())
print(ret.__next__())
