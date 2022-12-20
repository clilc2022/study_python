"""
题目：打印出杨辉三角形（要求打印出10行如下图）
"""


temp = []

for i in range(10):
    temp.append(1)
    result = temp[:]
    if i == 0:
        print(result)
        continue
    elif i == 1:
        print(result)
        continue
    else:
        for j in range(1, len(result) - 1):
            result[j] = temp[j] + temp[j - 1]
        temp = result[:]
        print(result)

