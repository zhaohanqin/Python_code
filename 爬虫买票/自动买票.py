# coding=utf-8
# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入动作链
from DrissionPage.common import Actions
# 导入键盘操作
from DrissionPage.common import Keys
# 中文转拼音
from pypinyin import pinyin, Style



def change(chinese):
    text=pinyin(chinese,style=Style.NORMAL)
    # print(text)
    string=''.join([i[0] for i in text])
    print(string)
    return string

def BUY(StartCity,ToCity,date,num):
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
    dp.ele(f'css:#queryLeftTable tr:nth-child({int(num)*2-1}) .btn72').click()
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
    dp.ele('css:#normalPassenger_0').click()  # 二号乘车人
    dp.ele('css:#submitOrder_id').click()  # 点击提交按钮
    # dp.ele('css:#qr_submit_id')#直接确定，如果要选座位的话，看添加点击选择座位的代码