import time
from multiprocessing import Process
from time import sleep


def func():
    for i in range(10):
        print("子进程工作中", i)
        sleep(0.2)
    print("子进程结束了")


if __name__ == '__main__':
    p1 = Process(target=func)
    # 设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
    p1.daemon = True
    p1.start()

    time.sleep(1)
    print("主进程结束了")

# 注意，这里打印出主进程结束，并不是意味着主进程已经结束了，主进程结束的标志是“进程已结束，退出代码为 0”
