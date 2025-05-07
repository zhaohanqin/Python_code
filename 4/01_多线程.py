# 线程，进程
# 进程是资源单位，每一个进程至少要有一个线程
# 线程是执行单位


from threading import Thread


def func():
    for i in range(1000):
        print(f"func {i}")


if __name__ == '__main__':
    t = Thread(target=func)
    t.start()  # 多线程状态为可以开始的工作状态，具体的执行时间由CPU决定
    for i in range(1000):
        print(f"main {i}")
