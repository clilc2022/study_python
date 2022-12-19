"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""

def print_diamond():
    for i in range(7):
        if i <= 3:
            print(" " * (3 - i) + "*" * (2 * i + 1))
        else:
            print(" " * (i - 3) + "*" * (2 * (6 - i) + 1))


if __name__ == "__main__":
    print_diamond()
