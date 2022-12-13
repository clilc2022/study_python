"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
"""


def complete_number(number):
    keys = []
    temp_number = number
    for i in range(1, number):
        if number % i == 0:
            temp_number -= i
            keys.append(i)
    if temp_number == 0:
        print(number)
        print(keys)


if __name__ == "__main__":
    for num in range(10001):
        complete_number(num)
