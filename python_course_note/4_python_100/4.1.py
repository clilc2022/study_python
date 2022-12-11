# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。


def test_1():
    list_1 = [1, 2, 3, 4]
    for i in list_1:
        for j in list_1:
            for k in list_1:
                if i != j and j != k and i != k:
                    print(i, j, k)


def test_2():
    list_1 = [1, 2, 3, 4]
    result = []
    temp = []

    def recursive(list_input, temp):
        if len(list_input) == 1:
            result.append(temp.copy())
            return
        else:
            for item in list_input:
                temp.append(item)
                temp_list_input = list_input.copy()
                temp_list_input.remove(item)
                recursive(temp_list_input, temp)
                temp.pop()

    recursive(list_1, temp)
    print(result)
    print(len(result))


if __name__ == "__main__":
    test_2()
