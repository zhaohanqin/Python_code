import xlwt

wb = xlwt.Workbook()
sh = wb.add_sheet('数据')

# 创建字体的样式
ft = xlwt.Font()
ft.name = '微软雅黑'  # 设置字体
ft.colour_index = 3  # 设置颜色
ft.height = 20 * 20  # 设置字体的大小，后面的（20）相当于计量单位，此时的11才是excel里面的11的大小
ft.bold = True  # 设置是否加粗
ft.underline = True  # 设置下划线
ft.italic = False  # 设置斜体

# 创建单元格的样式
# 设置单元格的的高度
# 设置单元格的的宽度
# 设置高度之前需要先做如下的操作
sh.row(3).height_mismatch = True
sh.row(3).height = 10 * 256  # 设置第三行的（所有）所有的高度
sh.col(3).width = 20 * 256  # 设置第三列的（所有）所有的宽度

# 设置输入的字体的位置的样式
alg = xlwt.Alignment()
alg.horz = 2  # 1 左，2 中，3 右
alg.vert = 1  # 0 上，1 中，2 下

# 设置边框的样式
border = xlwt.Borders()
# 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，
# 双线:6，细点虚线:7,花大粗虚线:8，细点划线:9，粗点划线:10，
# 细双点划线:11，祖双点划线:12、斜点团线:13
border.left = 5
border.right = 5
border.top = 5
border.bottom = 5
# 设置单元格的边框的颜色
border.left_colour = 10
border.right_colour = 2
border.top_colour = 3
border.bottom_colour = 4

# 设置单元格的背景的颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 全部填充
pattern.pattern_fore_colour = 7

# 设置字体
style1 = xlwt.XFStyle()
style1.font = ft

# 设置字体位置样式
style2 = xlwt.XFStyle()
style2.alignment = alg

# 设置边框
style3 = xlwt.XFStyle()
style3.borders = border

# 设置背景的颜色
style4 = xlwt.XFStyle()
style4.pattern = pattern

# 将设置的元素整合在一起
style = xlwt.XFStyle()
style.pattern = pattern
style.font = ft
style.alignment = alg
style.borders = border

sh.write(0, 0, '肖顺康')
sh.write(3, 4, '肖顺康123', style1)
sh.write(3, 3, '肖顺康123', style2)
sh.write(4, 4, '肖顺康456', style3)
sh.write(5, 5, '肖顺康789', style4)
sh.write(6, 6, '肖顺康999', style)

wb.save('04_设置样式.xlsx')
