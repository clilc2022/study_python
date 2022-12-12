"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
程序源代码
"""

month_list = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]


def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def what_days(year, month, day):
    result = 1 if is_leap_year(year) else 0
    result += day
    result += sum(month_list[:month-1])
    print(result)


if __name__ == "__main__":
    what_days(2015, 6, 7)
