"""
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
"""

def how_many_nine(num):
    if num % 2 == 0:
        return None
    count = 1
    temp = 9
    while True:
        if temp % num == 0:
            return count
        temp = temp * 10 + 9
        count += 1


print(how_many_nine(13))
