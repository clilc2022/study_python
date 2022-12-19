"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""

text = "abcde"

def reverse_print(text_str, len_text):
    if len_text == 0:
        return
    else:
        print(text_str[len_text - 1])
        reverse_print(text_str, len_text - 1)

reverse_print(text, len(text))
