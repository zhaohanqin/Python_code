import xlrd
from xlutils.copy import copy

read_book = xlrd.open_workbook('01_电影数据.xlsx')
sh = read_book.sheet_by_index(0)
# 复制数据
wb = copy(read_book)
# 复制出来的文件不能用这个方式来选择工作簿
# wb.sheet_by_index(0)
sh1 = wb.get_sheet(0)
sh1.write(5, 0, 'xskxsk')
sh1.write(5, 1, 123452345)
sh1.write(5, 2, 1.000)
sh1.write(5, 3, 10.0)

# 增加工作簿
sh2 = wb.add_sheet('汇总数据')

count = 0
# 这里的for循环不能在复制的sh1上面进行，只能在原来的xlsx上面读取到相应的工作簿以后，然后进行操作
for r in range(1, sh.nrows):
    num = sh.cell_value(r, 1)  # 索引是从01开始的，所以这里1代表的是电影的票房
    count += num
sh2.write(0, 0, 'count')
sh2.write(0, 1, f'{count}')

wb.save('03_电影数据（修改后）.xlsx')
