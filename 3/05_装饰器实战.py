login_flag = False


def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if not login_flag:
            print("请先登录:")
            while 1:
                name = input("请输入用户名:").strip()
                password = eval(input("请输入密码:").strip())
                if name == "admin" and password == 123:
                    print("登录成功")
                    login_flag = True
                    break
                else:
                    print("用户名或者密码输入有误")
        ret = fn(*args, **kwargs)
        str1 = str(fn)
        lst = str1.split(" ")
        # print(lst)
        print(lst[1] + "操作已完成")
        return ret

    return inner


@login_verify
def add():
    print("添加员工信息")


@login_verify
def upd():
    print("添加员工信息")


@login_verify
def search():
    print("1211435")


add()
search()
