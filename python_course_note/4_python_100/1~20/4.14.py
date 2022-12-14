"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True


def decompose(num):
    result_list = []
    if is_prime(num):
        result_list.append(num)
    else:
        while not is_prime(num):
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    result_list.append(i)
                    num = num // i
                    break
        result_list.append(num)
    return result_list


def prepare_output(num, result_list):
    output_str = f'{num} = '
    for i in range(len(result_list)):
        output_str += f'* {result_list[i]} ' if i != 0 else f'{result_list[i]} '
    print(output_str)


if __name__ == "__main__":
    for num in [90, 100]:
        prepare_output(num, decompose(num))

