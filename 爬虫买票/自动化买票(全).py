# coding=utf-8
import requests
# 导入制表模块
from prettytable import PrettyTable
# 导入json模块
import json
# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入动作链
from DrissionPage.common import Actions
# 导入键盘操作
from DrissionPage.common import Keys
# 中文转拼音
from pypinyin import pinyin, Style


def change(chinese):
    text = pinyin(chinese, style=Style.NORMAL)
    # print(text)
    string = ''.join([i[0] for i in text])
    print(string)
    return string


def BUY(StartCity, ToCity, date, num):
    # 打开浏览器
    dp = ChromiumPage()  # 实例化浏览器对象,此时会打开一个浏览器
    ac = Actions(dp)
    # 访问网址
    dp.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')
    """
    # 定位出发城市的输入框，进行输入
    dp.ele('css:#fromStationText').clear()
    dp.ele('css:#fromStationText').input('长沙')
    # 定位到达城市的输入框，进行输入
    dp.ele('css:#toStationText').clear()
    dp.ele('css:#toStationText').input('武汉')
    """
    ac.move_to('css:#fromStationText').click().type(change(StartCity))
    dp.ele('css:#fromStationText').input(Keys.ENTER)
    ac.move_to('css:#toStationText').click().type(change(ToCity))
    dp.ele('css:#toStationText').input(Keys.ENTER)
    # 定位日期输入框，进行输入
    dp.ele('css:#train_date').clear()
    dp.ele('css:#train_date').input(date)
    # 点击查询按钮
    dp.ele('css:#query_ticket').click()
    # 点击预定按钮
    dp.ele(f'css:#queryLeftTable tr:nth-child({int(num) * 2 - 1}) .btn72').click()  # 网页上的车的序号是显示出来的车的序号乘二以后再减一，（都是单数的）
    """判断是否有账号登录"""
    text = dp.ele('css:#login_user').text
    if text == '登录':
        # 输入账号
        dp.ele('css:#J-userName').input('13277487626')
        # 输入密码
        dp.ele('css:#J-password').input('Xsk20021018')
        # 点击登录
        dp.ele('css:#J-login').click()
        # 验证码
        dp.ele('css:#id_card').input('7653')
        dp.ele('css:#verification_code').click()
        code = input("请输入验证码").strip()
        dp.ele('css:#code').input(code)
        dp.ele('css:#sureClick').click()
    else:
        print('账号已登录')
    # 选择乘车人
    dp.ele('css:#normalPassenger_0').click()  # 一号乘车人
    dp.ele('css:#submitOrder_id').click()  # 点击提交按钮
    # dp.ele('css:#qr_submit_id')#直接确定，如果要选座位的话，看添加点击选择座位的代码


"""发送请求，请求标头"""
headers = {
    # 用户信息，常用于检查是由登陆账号（登录与否都有cookie）
    'Cookie': '_uab_collina=172621999617415761743271; '
              'JSESSIONID=F5579D308FBEAE07651EA7CD1BF52B51; '
              'BIGipServerotn=1339621642.64545.0000; '
              'BIGipServerpassport=904397066.50215.0000; '
              'guidesStatus=off; highContrastMode=defaltMode; '
              'cursorStatus=off; route=9036359bb8a8a461c164a04f8f50b252;'
              ' ''_jc_save_fromStation=%u957F%u6C99%2CCSQ; '
              '_jc_save_toStation=%u8D35%u9633%u5317%2CKQW;'
              ' _jc_save_fromDate=2024-09-14; '
              '_jc_save_toDate=2024-09-13; '
              '_jc_save_wfdc_flag=dc'
    ,
    # 用户代理，表示浏览器、设备 基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}
# 读取城市文件
# with open("city_data.json",mode="r",encoding="utf-8") as f:
f = open("city_data.json", encoding="GBK").read()
city_data = json.loads(f)  # 文件读取得到的数据类型是字符串类型的，要将字符串类型的数据转换为字典类型的数据
"""
print(f)
print(type(f))
print(city_data)
print(type(city_data))
"""
# 用户输入出发和目的城市
start_city0 = input("请输入出发的城市").strip()
end_city0 = input("请输入到达的城市").strip()
start_city = city_data[start_city0]
end_city = city_data[end_city0]
time = input("请输入查票的日期：（例如：2024-10-18）").strip()
# 请求网址
url = (f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={time}&leftTicketDTO.'
       f'from_station={start_city}&leftTicketDTO.to_station={end_city}&purpose_codes=ADULT')
# 发送请求
response = requests.get(url, headers=headers)
"""获取数据"""
# 获取响应的json数据
json_data = response.json()  # 得到的是字典格式的数据
"""
    #获取响应的文本数据
    text=response.text#得到的是字符串格式的文本
"""
"""解析数据"""
# 字典取值，取得字典里面的result的结果
result = json_data["data"]['result']
# 定义一个序号
page = 1
# 实例化对象
tb = PrettyTable()
# 设置字段名
tb.field_names = [
    '序号',
    '车次',
    '开始时间',
    '到达时间',
    '耗时',
    '二等座',
    '一等座',
    '特等座',
    '硬卧',
    '软卧',
    '硬座',
    '无座'
]
# for循环遍历，提取列表里面的元素
for item in result:
    # 进行字符串分割，返回的是一个列表，打印列表里面的元素
    item = item.split('|')
    # 获得相关的位置信息
    car_num = item[3]
    start_time = item[8]
    end_time = item[9]
    use_time = item[10]
    second_class = item[30]
    first_class = item[31]
    topGrade = item[32]
    hard_sleeper = item[28]
    soft_sleeper = item[23]
    hard_seat = item[29]
    no_seat = item[26]
    dit = {
        '车次': car_num,
        '开始时间': start_time,
        '到达时间': end_time,
        '耗时': use_time,
        '二等座': second_class,
        '一等座': first_class,
        '特等座': topGrade,
        '硬卧': hard_sleeper,
        '软卧': soft_sleeper,
        '硬座': hard_seat,
        '无座': no_seat
    }
    # 添加数据内容
    tb.add_row([
        page,
        car_num,
        start_time,
        end_time,
        use_time,
        second_class,
        first_class,
        topGrade,
        hard_sleeper,
        soft_sleeper,
        hard_seat,
        no_seat
    ])
    page += 1
print(tb)
train_num = input('输入想要购买的车次')
BUY(StartCity=start_city0, ToCity=end_city0, date=time, num=train_num)
