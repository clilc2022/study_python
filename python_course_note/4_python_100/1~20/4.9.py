"""暂停一秒输出"""
import time

temp = [_ for _ in range(10)]
for item in temp:
    print(item)
    time.sleep(1)