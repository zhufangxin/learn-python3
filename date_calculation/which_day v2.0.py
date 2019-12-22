"""
功能：根据用户输入的日期判断这是今年的第几天
新增功能： 用列表替换元组
"""
from datetime import datetime


def is_leap_year(year):
    is_leap_year = False
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        is_leap_year = True
    return is_leap_year


def main():
    input_str_date = input('请输入日期：')
    input_date = datetime.strptime(input_str_date, '%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]
    if is_leap_year(year):
        days_in_month_list[1]=29
    # 计算之前月数的天数总和和当前月的天数
    days = sum(days_in_month_list[:month - 1]) + day

    print('这是第{}天'.format(days))


if __name__ == '__main__':
    main()
