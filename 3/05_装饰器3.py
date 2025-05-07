"""
内容回顾：
    1.函数可以作为参数进行传递
    2.函数可以作为返回值返回
    3.函数可以像变量一样进行赋值操作

装饰器：可以直接记住最后的结论
     本质上是一个闭包
     作用：不改变原有的函数的调用的情况下，给函数添加新的功能
     即：在函数前后添加新的功能，但是不改变原来的代码


     在用户登录的地方，日志等方面有很大的作用
     雏形：
     def wrapper(fn):
        def inner():
            #在目标执行之前完成的操作
            fn()
            #在目标执行后完成的操作
        return inner   #这里一定不能加上小括号


    通用的装饰器的写法：
     def wrapper(fn):
        def inner(*args, **kwargs):
            #在目标执行之前完成的操作
            ret = fn(*args, **kwargs)
            #在目标执行后完成的操作
            return ret
        return inner   #这里一定不能加上小括号

"""


# def guanjia(game):  # 设定一个游戏管家，让管家帮忙执行打开和关闭外挂的操作
#     def inner(*args, **kwargs):  # inner添加了参数，args一定是一个元组，kwargs一定是一个字典
#         print("打开外挂")
#         ret = game(*args, **kwargs)  # 这里的*和上面的*不一样，这里的表示将args和kwargs打散成位置参数和关键字参数,如果这里没有使用*和**后面打印的就是元组和字典格式
#         print("关闭外挂")
#         return ret
#
#     return inner
#
#
# @guanjia  # 相当于play_dnf = guanjia(play_dnf)的操作
# def play_dnf(username, password):
#     print("12345dnf", username, password)
#     return "爆的装备"
#
#
# @guanjia  # play_lol = guanjia(play_lol)
# def play_lol(username, password, hero):
#     print("德玛西亚！！！！！！！！！", username, password, hero)
#     return "胜率"
#
#
# ret1 = play_dnf("12123131", "123131231")
# ret2 = play_lol("123124", 1241412, "gailun")
# print(ret1, ret2)

def wrapper1(fn):  # 此时的fn是wrapper2.inner
    def inner(*args, **kwargs):
        print("wrapper1in")  # 1
        ret = fn(*args, **kwargs)
        print("wrapper1out")  # 5
        return ret

    return inner


def wrapper2(fn):  # 此时的fn是target
    def inner(*args, **kwargs):
        print("wrapper2in")  # 2
        ret = fn(*args, **kwargs)
        print("wrapper2out")  # 4
        return ret

    return inner


# 一个函数被多个装饰器装饰的结果：
# wrapper1 wrapper2 target wrapper2 wrapper1
@wrapper1  # target=wrapper1(wrapper2.inner)  :此时的target:wrapper1.inner
@wrapper2  # target=wrapper2(target)  :此时的target:wrapper2.inner
def target():
    print("我是目标函数")  # 3


target()
