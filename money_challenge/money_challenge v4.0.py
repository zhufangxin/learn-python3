"""
功能：用户自己设置每周存入胡金额 递增的金额和存几周
"""
import math


def save_money_for_n_weeks(total_week, money_per_week, increase_money):
    money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, total_money))
        money_per_week += increase_money
    return total_money


def main():
    total_week = int(input('请输入要存的周数：'))
    money_per_week = float(input('请输入每周存钱数：'))  # 每周存入的金额
    increase_money = float(input('请输入递增的金额：'))  # 递增的金额
    total_money = save_money_for_n_weeks(total_week, money_per_week, increase_money)
    print('总存款金额', total_money)


if __name__ == '__main__':
    main()
