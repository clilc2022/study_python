"""
题目：输入3个数a,b,c，按大小顺序输出。
"""


def print_max_min(list_input):
    list_input.sort(reverse=True)
    for item in list_input:
        print(item)


print_max_min([456, 123, 789])
