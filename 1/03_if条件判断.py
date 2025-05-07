# 第一种语法
money = 500
if money > 300:
    print("1234")
    print("56789")
print("00000")

# 第二种语法
money = eval(input("请输入你的钱:"))
if money > 500:
    print("123")
else:
    print("456")

# 第三种语法
# if的嵌套

# 第四种语法，条件if
if money > 200:
    print("123")
elif money > 200 and money < 500:
    print("456")
elif money > 500 and money < 1000:
    print("789")
