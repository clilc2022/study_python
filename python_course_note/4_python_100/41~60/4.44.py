"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
"""


import numpy as np

aaa = np.arange(9).reshape((3, 3))
bbb = np.random.randint(0, 10, (3, 3))

print(aaa)
print(bbb)
print(aaa + bbb)