"""
递归：函数直接调用自己
没有任何东西拦截的情况下是一个死循环
"""


def fun():
    print(123456)
    fun()


def fun2(n):
    if n == 0:
        return 1
    else:
        return n * fun2(n - 1)


print(fun2(3))
