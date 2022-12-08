

def main():
    list1 = [_ for _ in range(10)]
    list2 = [_ for _ in range(0, 20, 2)]

    print(list1 + list1)
    print(list1 * 2)

    list1.extend(list2)
    print(list1)
    list1.append(100)
    print(list1)
    list1.insert(1, 3)
    print(list1)

    pop_item = list1.pop()
    print(pop_item, list1)
    del list1[9]
    print(list1)
    list1.remove(10)
    print(list1)

    print(list1.count(2))
    print(list1.index(2))
    list1.reverse()
    print(list1)


if __name__ == "__main__":
    main()
