"""
1.算术运算  + - * / %(得到余数) //(得到整除的数)
2.比较运算  == < > <= >= !=
3.赋值运算  = +=
4.逻辑运算 and or not 运算顺序：先算括号>再算not>再算and>再算or
5.成员运算 in                                     not in
"""

# 3.赋值运算
a = 20
b = 10

a = b
b = a
print(a)
print(b)

a = 20
b = 10
a, b = b, a
print(a)
print(b)
