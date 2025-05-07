""""
参数：可以在函数调用时，给函数传递一些信息

分类：
    1.形参，在函数定义的时候，需要准备一些变量来接受信息
        （1）位置参数，按照位置一个一个地声明变量
        （2）默认值参数，在函数声明的时候给变量一个默认值，如果实参不传递信息，则此默认值生效，反之就不生效
        顺序：位置>默认值参数
        （3）动态参数
            1.*args，表示接受所有的位置参数的动态传参
            2.**kwargs,表示的是关键字参数的动态传参

        顺序：位置参数 > *args > 默认值参数 > **kwargs

    2.实参，实际在调用的时候传递信息
    （1）位置参数，按照位置进行传参
    （2）关键字参数，按照参数的名字来进行参数的传递
    （3）混合参数
        顺序：位置参数在前面，关键字参数在后面
    执行的时候，形参必须要有数据


"""


def luru(name, age, gender="男"):
    print(name, age, gender)


def chi1(zhu, fu, tang, tian):
    print(zhu, fu, tang, tian)


def chi2(*food):  # * 表示的是位置参数的动态传递，* 接受到的值被统一放到一个元组里面了
    print(food)


def chi3(**food):  # ** 表示的是关键字参数的动态传递，** 接受到的所有参数会被处理为字典
    print(food)


def func(a, b, c="哈哈", *args, **kwargs):
    print(a, b, c, args, kwargs)


def func2(a, b, *args, c="哈哈", **kwargs):
    print(a, b, c, args, kwargs)


def fun3(*args):
    print(args)


luru("xsk", 21)
luru("lqq", 21, "女")
chi1("damifan", "sss", "asdfa", "asdad")
chi2("damifan", "sss", "asdfa", "asdad")  # * 接受到的值被统一放到一个元组里面了
chi3(zhu="damifan", fu="damifan", tang="damifan", tian="damifan")  # ** 接受到的所有参数会被处理为字典
func(1, 2, 3, 4, 5, 6, 7, 8, 9, hello="12345")  # 此时C被覆盖了
func(1, 2, hello="12345")  # *agrs如果可以收到值，则c一定会被覆盖
func2(1, 2, 3, 4, 5, 6, 7, 8, 9, hello="12345")  # 如果c不想被覆盖，*args必须在c的前面

# 补充
stu_lst = ["xsk", "zhq", "skx", "hqz", "xsk", "zhq", "skx", "hqz", "xsk", "zhq", "skx", "hqz", "xsk", "zhq", "skx",
           "hqz", "xsk", "zhq", "skx", "hqz", "xsk", "zhq", "skx", "hqz", "xsk", "zhq", "skx", "hqz"]
fun3(*stu_lst)  # *在实参位置出现的话，是将列表打散为位置参数进行传递，
                # 同理**在实参位置可以把字典自动转换为关键字参数进行传递
