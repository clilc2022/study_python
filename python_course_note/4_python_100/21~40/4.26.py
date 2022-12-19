"""
题目：利用递归方法求5!
"""

def fact(i):
    result = 0
    if i == 1:
        result = 1
    else:
        result = i * fact(i - 1)
    return result

print(fact(5))
