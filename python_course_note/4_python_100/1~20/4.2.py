# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。

input_profit = 50000
interest = [0, 10, 20, 40, 60, 100]
interest = [i * 10000 for i in interest]
rate = [0, 10, 7.5, 5, 3, 1.5, 1]
rate = [i * 0.01 for i in rate]
get = [0] + [(interest[i] - interest[i - 1]) * rate[i] for i in range(1, len(interest))]
for i in range(1, len(interest)):
    get[i] += get[i - 1]

interest.reverse()
rate.reverse()
get.reverse()

for i in range(len(interest)):
    if input_profit < interest[i]:
        continue
    else:
        result = get[i] + (input_profit - interest[i]) * rate[i]
        break

print(result)


