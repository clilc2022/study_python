"""
题目：求100之内的素数
"""
import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(100):
        if is_prime(i):
            print(i)
