"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b) ? a:b 这是条件运算符的基本例子。
"""

def get_rank(score):
    if score >= 90:
        rank = "A"
    elif score>= 60:
        rank = "B"
    else:
        rank = "C"
    return rank

if __name__ == "__main__":
    score_list = [100, 90, 80, 60, 50]
    for score in score_list:
        print(get_rank(score))
