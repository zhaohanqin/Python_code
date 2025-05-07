import requests
import json
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9053"
print("正在获取数据。")
# 发送请求，获取返回的数据
res = requests.get(url)
data = str(res.content, encoding="utf8")
dict_data = dict()
# 根据'|'分隔数据
list_data = data.split('|')
# 从下标'1'开始, 每间隔5个为字典key
result_x = list_data[1:len(list_data):5]
# 从下标'2'开始, 每间隔5个为字典value
result_y = list_data[2:len(list_data):5]
# 循环将数据写入字典
for i in range(len(result_x)):
    dict_data[result_x[i].replace(" ", "")] = result_y[i]
# print(dict_data)
json_data = json.dumps(dict_data, indent=1, ensure_ascii=False)
with open("city_data.json", 'w') as w:
    w.write(json_data)
    print("数据保存完成！")


