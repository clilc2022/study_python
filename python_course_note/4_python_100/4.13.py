"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
"""

def is_shui_xian_hua(num):
    str_num = str(num)
    if len(str_num) != 3:
        return False
    temp = sum([int(str_num[i]) ** 3 for i in range(3)])
    if temp == num:
        return True
    return False


if __name__ == "__main__":
    for i in range(100, 1000):
        if is_shui_xian_hua(i):
            print(i)
