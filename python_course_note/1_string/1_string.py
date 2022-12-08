

def main():
    var1 = "hello world!"

    # joint
    print(var1 + var1)

    # multiply
    print(var1 * 3)

    # in / not in
    print('hello' in var1)
    print('aaaa' in var1)

    # format
    print(f"This is {var1}")
    print("This is {}".format(var1))

    # build-in
    print(var1.capitalize())
    print(var1.count('l'))
    print(var1.endswith('!'))
    print(var1.find('aaa'))
    print(var1.find('ll'))
    print("123aaa".isalnum())
    print("aaa".isalpha())
    print("123".isdigit())
    print("--".join(['1','2','3']))
    print(var1.partition('ll'))
    print(var1.partition('aa'))
    print("aallaallaall".partition('ll'))
    print("aallaallaall".split('ll'))
    print("aallaallaall".translate(str.maketrans('ll', 'bb')))
    import string
    print("a!a@l#l$a%a^l&l*a,a.l?l(".translate(str.maketrans("", "", string.punctuation)))


if __name__ == "__main__":
    main()
    