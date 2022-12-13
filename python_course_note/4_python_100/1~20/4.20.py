"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

def ball_fall(num, height):
    result = 0
    for i in range(num):
        result += height if i == 0 else 2 * height
        height /= 2
    return result, height


if __name__ == "__main__":
    print(ball_fall(10, 100))


