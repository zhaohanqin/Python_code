import xlwt

# 创建一个excel
wb = xlwt.Workbook()
# 选择工作簿
sh = wb.add_sheet('电影')
# 写入数据 到单元格
# 第一个数字是行，第二个数字是列，索引从0开始
sh.write(0, 0, '电影名称')
sh.write(0, 1, '电影票房')
sh.write(0, 2, '票房占比')
sh.write(0, 3, '评分')

sh.write(1, 0, '复仇者联盟')
sh.write(1, 1, 1599)
sh.write(1, 2, 0.99)
sh.write(1, 3, 9.9)

sh.write(2, 0, '钢铁侠')
sh.write(2, 1, 15991)
sh.write(2, 2, 0.991)
sh.write(2, 3, 9.91)

sh.write(3, 0, '蜘蛛侠')
sh.write(3, 1, 15992)
sh.write(3, 2, 0.992)
sh.write(3, 3, 9.92)

sh.write(4, 0, '肖申克的救赎')
sh.write(4, 1, 15999)
sh.write(4, 2, 0.999)
sh.write(4, 3, 9.99)
# 保存excel
wb.save('01_电影数据.xlsx')
