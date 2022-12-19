"""
题目：求1+2!+3!+...+20!的和。
"""

temp = []

for i in range(1, 21):
    if i == 1:
        temp.append(i)
    else:
        temp.append(i * temp[-1])

print(sum(temp))
