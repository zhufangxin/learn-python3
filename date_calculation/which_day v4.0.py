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
    day_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    days = 0
    days += day
    for i in range(1, month):
        days += day_month_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1
    print('这是第{}天'.format(days))


if __name__ == '__main__':
    main()
