"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
问最后留下的是原来第几号的那位。
"""


def solution(n, number):
    number_list = [_ for _ in range(1, n + 1)]
    count = 0
    while True:
        temp = number_list.pop(0)
        count += 1
        if count == number:
            count = 0
            continue
        number_list.append(temp)
        if len(number_list) == 1:
            return number_list[0]


print(solution(34, 3))


