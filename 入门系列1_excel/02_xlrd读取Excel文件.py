import xlrd

# 打开excel
wb = xlrd.open_workbook('01_电影数据.xlsx')

# 获取对应的工作簿
print(f'wb中有{wb.nsheets}个工作簿')
print(f'wb中的工作簿的名字是{wb.sheet_names()}')  # 返回的是一个列表

# 选择工作簿
# 可以通过索引和通过名字两种方式来进行选择
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('Sheet1')

print(f'sh1里面有{sh1.nrows}行，{sh1.ncols}列的数据')

# 获取单元格的值，三种不同的方法
print(f'第一行第二列的数据为:{sh1.cell_value(0, 1)}')  # 直接通过索引拿到数据
print(f'第一行第二列的数据为:{sh1.cell(0, 1).value}')  # 先找到对应的单元格，然后拿取数据
print(f'第一行第二列的数据为:{sh1.row(0)[1].value}')  # 先找行，再找列，然后拿数据

# 获取整行或者整列的数据，返回的是列表
print(sh1.row_values(0))  # 第一行
print(sh1.col_values(0)[1:])  # 第一列

# 遍历所有的数据
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'{sh1.cell_value(r, c)}', end='  ')
    print()  # python里面的print函数自己就带有一个换行符
