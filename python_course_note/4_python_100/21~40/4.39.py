"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""

def insert_num(num, sorted_list):
    len_list = len(sorted_list)
    i = 0
    while sorted_list[i] < num:
        i += 1
    sorted_list.insert(i, num)


sorted_list = [_ for _ in range(10)]
insert_num(5.5, sorted_list)
print(sorted_list)

