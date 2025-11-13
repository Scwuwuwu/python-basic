"""
    条件分支:
        - 单分支
        - 双分支
        - 多分支
        - 嵌套分支
"""


# 多分支
age = int(input("输入年龄"))
# if age < 18:
#     print("未成年")
# elif age >= 18 & age <= 30:
#     print("青年")
# else:
#     print("老年")

# 嵌套分支
msg = input("是否体检;是/否")
level = int(input("会员等级为: "))
if age > 18 & age < 45:
    if msg == "是":
        if level == 1:
            print("纪念T恤")
        elif level == 2:
            print("跑鞋")
        else:
            print("耳机")
    else:
        print("未体检不能参加比赛")
else:
    print("年龄不通过,不能参加比赛")