"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""

def solution(num):
    result = 0
    if num % 2 == 0:
        for i in range(1, num // 2 + 1):
            result += 1 / (i * 2)
        return result
    else:
        for i in range(1, num // 2 + 2):
            result += 1 / (i * 2 - 1)
        return result


print(solution(6))