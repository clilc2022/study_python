"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

import numpy as np


def solution(list_input):
    print(list_input)
    max_index = np.argmax(list_input)
    min_index = np.argmin(list_input)

    def swap(a, b):
        list_input[a], list_input[b] = list_input[b], list_input[a]

    swap(0, max_index)
    swap(-1, min_index)
    print(list_input)


list_input = np.random.randint(0, 10, 10)
solution(list_input)
