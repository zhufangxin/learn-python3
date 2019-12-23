"""
功能：根据用户输入的日期判断这是今年的第几天
新增功能： 根据天数将月份化为不同的集合再计算
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
    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    days = 0
    days += day
    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month>2:
        days += 1
    print('这是第{}天'.format(days))


if __name__ == '__main__':
    main()
