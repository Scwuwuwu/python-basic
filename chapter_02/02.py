"""
    循环:
        - while
        - for
    流程控制:
        - continue: 跳过此次循环
        - break: 结束循环
"""

# while eg: 回答问题
question = "你是谁"
ans = "SC"
resp = input(f"{question}?")
while resp != ans:
    print("错误")
    resp = input(f"{question}?")

# for   eg: 文字加密
msg = "哈基米"
res = ""
for n in msg:
    unicode = ord(n)
    res += chr(unicode + 1)
print(res)


# 嵌套循环
for row in range(1,10):
    for item in range(1,row + 1):
        print(f'{row} * {item} = {row * item}',end='\t')
    print()

