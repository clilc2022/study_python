"""
题目：809*??=800*??+9*??
其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
求??代表的两位数，及809*??后的结果。
"""


def weishu(num):
    return len(str(num))


for i in range(10, 100):
    if (weishu(809 * i) == 4 and weishu(8 * i) == 2 and
        weishu(9 * i) == 3 and (809 * i == (800 * i + 9 * i))):
        print(i)
        print(809 * i)