"""
功能：52周存钱计划
week saving total
1     10     10
2     20     30
3     30     60
4     40     100
...
知识点： List, math
"""
import math


def main():
    week = 1
    total_week = 52
    money_per_week = 10  # 每周存入的金额
    increase_money = 10  # 递增的金额
    money_list = []

    while week <= total_week:
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(week, money_per_week, total_money))
        week += 1
        money_per_week += increase_money


if __name__ == '__main__':
    main()
