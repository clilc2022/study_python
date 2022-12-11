import string
import copy


def main():
    temp = dict.fromkeys([_ for _ in range(10)], 0)
    print(temp)

    dict_test = dict(zip(string.ascii_lowercase, [_ for _ in range(1, 27)]))
    print(dict_test)

    dict_test['aaa'] = 100
    print(dict_test)

    del dict_test['aaa']
    print(dict_test)

    temp_s = dict_test.copy()
    temp_d = copy.deepcopy(dict_test)
    print(id(temp_s))
    print(id(temp_d))
    print(temp_s)
    print(temp_d)

    temp_s.clear()
    print(temp_s)

    print(dict_test.get('b', 0))
    print(dict_test.items())
    print(dict_test.keys())
    print(dict_test.values())



if __name__ == "__main__":
    main()
