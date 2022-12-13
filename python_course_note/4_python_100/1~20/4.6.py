"""题目：斐波那契数列"""


def fib1(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)