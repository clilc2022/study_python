"""
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
"""


if __name__ == "__main__":
    n = 0
    while n < 7:
        num = int(input("input a number in 1~50:"))
        if 1 <= num <= 50:
            print('*' * num)
            n += 1
        else:
            continue
