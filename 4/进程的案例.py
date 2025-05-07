from multiprocessing import Process
import os


def copy(file_name, source_dir, dest_dir):
    # 1.拼接源文件的路径和目标文件的路径
    source_path = source_dir + "/" + file_name  # 源文件的路径
    dest_path = dest_dir + "/" + file_name  # 目标文件的路径
    print(source_path, "----->", dest_path)
    with open(source_path, "rb") as s:
        try:
            with open(dest_dir, "wb") as d:
                while True:
                    data = s.read()
                    if data:
                        d.write(data)
                    else:
                        break
        except PermissionError:
             print("没有足够的权限写入文件")


if __name__ == '__main__':

    # 1.定义原文件夹和目标文件夹
    source_dir = r'D:\pycharm\python_begineer\1'
    dest_dir = r'C:\Users\Administrator\Desktop\test01'
    try:
        # 2.创建出目标文件夹目录
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已存在")

    # 3.读取源文件夹下的文件列表
    file_list = os.listdir(source_dir)

    # 4.对源文件夹下面的文件进行操作
    for i in file_list:
        p = Process(target=copy, args=(i, source_dir, dest_dir))
        p.start()
