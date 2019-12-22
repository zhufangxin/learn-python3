"""
功能：52周存钱计划
week saving total
1     10     10
2     20     30
3     30     60
4     40     100
...
"""


def main():
    week = 1
    saving_money = 10
    total_money = 0
    while week <= 52:
        total_money += saving_money
        print('第{}周，存钱{}元，总共存钱{}元'.format(week, saving_money, total_money))
        week += 1
        saving_money += 10

if __name__ == '__main__':
    main()
