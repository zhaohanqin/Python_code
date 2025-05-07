import xlwt
import xlrd
from xlutils.copy import copy

"""
#建立相应的表格

wb=xlwt.Workbook()
sh=wb.add_sheet('案例1')

sh.write(0,0,'A')
sh.write(0,1,'水果')
sh.write(0,2,'苹果')
sh.write(0,3,100)
sh.write(0,4,3.5)

sh.write(1,0,'A')
sh.write(1,1,'水果')
sh.write(1,2,'香蕉')
sh.write(1,3,100)
sh.write(1,4,3.2)

sh.write(2,0,'A')
sh.write(2,1,'水果')
sh.write(2,2,'葡萄')
sh.write(2,3,100)
sh.write(2,4,3)

sh.write(3,0,'A')
sh.write(3,1,'水果')
sh.write(3,2,'椰子')
sh.write(3,3,100)
sh.write(3,4,6)

sh.write(4,0,'A')
sh.write(4,1,'水果')
sh.write(4,2,'榴莲')
sh.write(4,3,100)
sh.write(4,4,15)

list_B=['热水器','压力锅','空气炸锅','体重秤','电吹风']
list_C=['酸奶','速冻面点','午餐肉','儿童零食']

for r in range(5,10):
        sh.write(r,0,'B')
        sh.write(r,1,'生活用品')
        sh.write(r,2,list_B[r-5])
        sh.write(r,3,35)
        sh.write(r,4,60)

for r in range(10,14):
        sh.write(r,0,'C')
        sh.write(r,1,'零食')
        sh.write(r,2,list_C[r-10])
        sh.write(r,3,100)
        sh.write(r,4,60)

wb.save('05_数据汇总案例.xlsx')
"""


def read_data():
    wb = xlrd.open_workbook('05_数据汇总案例.xlsx')
    sh = wb.sheet_by_index(0)
    fen_data = {}
    count_price = []

    for r in range(sh.nrows):
        count = sh.cell(r, 3).value * sh.cell_value(r, 4)
        count_price.append(count)
        key = sh.cell_value(r, 0)
        if fen_data.get(key):
            fen_data[key] += count
        else:
            fen_data[key] = count

    return fen_data, count_price  # 返回的是各个分类的总的价值和每个单品的总的价值


def save(fen, counnt):
    wb = xlrd.open_workbook('05_数据汇总案例.xlsx')
    sh1 = wb.sheet_by_index(0)

    wb2 = copy(wb)
    sh2 = wb2.get_sheet(0)
    for r in range(sh1.nrows):
        sh2.write(r, sh1.ncols, counnt[r])  # 这里sh1.ncols返回的是一个数（列的个数）,由于这里没有从零开始取，所以得到的数刚好可以加一列出来

    sh3 = wb2.add_sheet('汇总的数据')  # 建立一个新的工作簿
    for i, d in enumerate(fen):  # 这里使用枚举的形式，第一个返回的参数是字典里面的key对应的索引的大小，第二个返回的参数是字典的key
        sh3.write(i, 0, d)  # 字典里面的key的种类只有三种，所以i只能是0，1，2；d就是对应的key
        sh3.write(i, 1, fen.get(d))  # 取出字典里面key对应的值

    wb2.save('05.xlsx')


if __name__ == '__main__':
    f, c = read_data()
    save(f, c)
