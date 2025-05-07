import xlrd
from xlutils.copy import copy


def get_data():
    wb = xlrd.open_workbook('05_数据汇总案例.xlsx')
    sh = wb.sheet_by_index(0)

    all_data = {}  # 用来存放总的数据
    # 从工作簿里面取数据出来,将取出来的数据按每一行放置到一个列表里面
    for i in range(sh.nrows):
        d = {'type': sh.cell(i, 1).value, 'name': sh.cell_value(i, 2), 'count': sh.cell_value(i, 3),
             'price': sh.cell_value(i, 4)}
        key = sh.cell(i, 0).value  # 厂家的名称作为类别，价格数据分开存放
        if all_data.get(key):
            all_data[key].append(d)
        else:
            all_data[key] = [d]  # 如果数据不存在的话，就放一个列表用来存放对应的每一行的数据,每一行的数据都是字典，{a:[{},{}],b:[{},{}],c:[{},{}]}
    return all_data


def save_data(data):
    wb = xlrd.open_workbook('05_数据汇总案例.xlsx')
    sh = wb.sheet_by_index(0)
    wb2 = copy(wb)
    for key in data.keys():
        temp_sheet = wb2.add_sheet(key)  # 按照厂家的名字来创建工作簿
        for i, d in enumerate(data.get(key)):  # data.get(key)这里得到是一个列表，列表里面的元素是每一行数据（以字典的形式保存的）
            temp_sheet.write(i, 0, d.get('type'))
            temp_sheet.write(i, 1, d.get('name'))
            temp_sheet.write(i, 2, d.get('count'))
            temp_sheet.write(i, 3, d.get('price'))

    wb2.save('06_表格的拆分.xlsx')
    print('表格已保存')


if __name__ == '__main__':
    all_data = get_data()
    # print(all_data.get('A'))
    save_data(all_data)
