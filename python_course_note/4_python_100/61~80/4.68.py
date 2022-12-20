"""
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
"""


temp = [_ for _ in range(10)]
n = 3

for _ in range(n):
    local_temp = temp[:]
    local_temp.insert(0, local_temp.pop())
print(local_temp)


