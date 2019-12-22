"""
功能：用户自己输入日期，系统判断是第几周，输出这周对应的账户累计金额
知识点： datetime库
"""
import datetime
import math


def save_money_for_n_weeks(total_week, money_per_week, increase_money):
    money_list = []
    saved_money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        total_money = math.fsum(money_list)  # 当前总金额
        saved_money_list.append(total_money)  # 每周对应的金额列表
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, total_money))
        money_per_week += increase_money
    return saved_money_list


def main():
    total_week = int(input('请输入要存的周数：'))
    money_per_week = float(input('请输入每周存钱数：'))  # 每周存入的金额
    increase_money = float(input('请输入递增的金额：'))  # 递增的金额
    saved_money_list = save_money_for_n_weeks(total_week, money_per_week, increase_money)
    inp_str_date = input('请输入日期(yyyy/mm/dd)：')
    inp_date = datetime.datetime.strptime(inp_str_date, '%Y/%m/%d')  # string pass time
    week_num = inp_date.isocalendar()[1]  # 第几周

    print('第{}周的存款总金额为{}'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()
