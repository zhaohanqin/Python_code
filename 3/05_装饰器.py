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

"""


def guanjia(game):  # 设定一个游戏管家，让管家帮忙执行打开和关闭外挂的操作
    def inner():
        print("打开外挂")
        game()
        print("关闭外挂")

    return inner


@guanjia  # 相当于play_dnf = guanjia(play_dnf)的操作
def play_dnf():
    print("12345dnf")


@guanjia  # play_lol = guanjia(play_lol)
def play_lol():
    print("德玛西亚！！！！！！！！！")


# play_dnf = guanjia(play_dnf)  # 让管家把游戏重新封装了一下，把原来的游戏给替换掉
# play_lol = guanjia(play_lol)  # 让管家把游戏重新封装了一下，把原来的游戏给替换掉

play_dnf()
play_lol()
