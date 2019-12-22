"""
功能：根据用户输入的日期判断这是今年的第几天
"""
from datetime import datetime


def main():
    input_str_date = input('请输入日期：')
    input_date = datetime.strptime(input_str_date, '%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month = (31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31)
    # 计算之前月数的天数总和和当前月的天数
    days = sum(days_in_month[:month - 1]) + day
    # 如果是闰年多加一天（四年一闰，百年不闰，四百年再闰）
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        if month > 2:
            days += 1
    print('这是第{}天'.format(days))


if __name__ == '__main__':
    main()
