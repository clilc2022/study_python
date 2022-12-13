"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

def count_alpha_space_digit(input_str):
    count_dict = dict.fromkeys(['alpha', 'space', 'digit', 'other'], 0)
    for item in input_str:
        if item.isalpha():
            count_dict['alpha'] += 1
        elif item.isdigit():
            count_dict['digit'] += 1
        elif item.isspace():
            count_dict['space'] += 1
        else:
            count_dict['other'] += 1
    return count_dict


if __name__ == "__main__":
    input_str = "ashfdi123123   afdsf1323,./.,!"
    count_dict = count_alpha_space_digit(input_str)
    print(count_dict)
