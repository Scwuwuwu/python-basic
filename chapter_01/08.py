"""
字符串:
    - 格式化输出
    - 精度控制
    - 转义字符
"""

# 格式化输出

name = "sc"
age = 12
weight = 13.236

# 使用f-string
print(f"我是{name},年龄是{age},体重为:{weight}")

"""
    %m.nf
        n: 精度控制;控制输出的最大位数(如果大于字符串最大长度则无效) 
"""
msg1 = "体重为:%.2f" % weight
msg2 = "体重为:%.1f" % weight
print(msg1)
print(msg2)

# 转义字符
# \' => '
m1 = '这是单引号\''
print(m1)

# \" => "
m2 = "这是双引号\""
print(m2)
# \n换行
m3 = f'我是sc\nage为: {age}\n体重为:{weight}'
print(m3)
# \\ => \
m4 = "这是反斜杠\\"
print(m4)
# \b消除上个字符
m5 = "helloo\b"
print(m5)
# \r内容覆盖
m6 = "30%\r60"
print(m6)
# \t
m7 = "abc\tde"
print("1234123412341234")
print(m7)

