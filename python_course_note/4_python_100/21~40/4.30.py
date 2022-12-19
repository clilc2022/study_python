"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""

def is_huiwen(input_str):
    input_str = str(input_str)
    len_str = len(input_str)
    if len_str == 1:
        return True
    for i in range(int(len_str/2)):
        if input_str[i] != input_str[len_str-i-1]:
            return False
    return True


print(is_huiwen("12321"))
print(is_huiwen("123421"))
