i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
    if i == 10:
# break  结束循环，此时会直接退出整个while循环
# continue 跳出此次的循环，还会执行下一次的循环
        pass
print(sum)
