"""
    进制转换:
        十 -> other:         转换为字符串
            bin()   2
            oct()   8
            hex()   16
        other -> 10:
            int(val,原进制)    转换为数字
"""
# 2other
res1 = bin(10)
res2 = oct(10)
res3 = hex(10)
print(res1,res2,res3)
print(type(res1))

# other2,待转换的数据类型必须为String
s1 = "0b1010"
r1 = int(s1,2)
# r2 = int(0o12,8)
# r3 = int(0xa,16)
# print(r1,r2,r3)
print(r1)
print(type(r1))
