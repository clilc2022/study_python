"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

def diff_sum(a, b):
    result = 0
    mark = 1
    for i in range(1, b + 1):
        result += int(str(mark) * i)
    return (result * a)

if __name__ == "__main__":
    print(diff_sum(a=4, b=4))
