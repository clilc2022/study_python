"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

input_str = "12345"

print(len(input_str))
for i in range(len(input_str)-1, -1, -1):
    print(input_str[i])
    