# 1.字符集和编码
s = "周杰伦"
ds = s.encode("gbk")  # b'XXXX'bytes类型 6个字节
ds1 = s.encode("utf-8")  # 9个字节
print(ds)
print(ds1)

# 将gbk的类型转换为utf-8
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'  # gbk
# 先将其变为文字符号(字符串)
s = bs.decode("gbk")  # 解码
bs1 = s.encode("utf-8")  # 编码
print(bs1)
print(bs1.decode())
