"""
题目：判断101-200之间有多少个素数，并输出所有素数
"""
import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True


if __name__ == "__main__":
    count = 0
    for i in range(101, 201):
        if is_prime(i):
            count += 1
            print(i)
    print(count)

