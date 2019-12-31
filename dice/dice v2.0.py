"""
功能：模拟掷两个骰子，计算两个骰子的点数之和　以及出现的次数频率
知识点:zip(key,value) 返回元组。由于元组不能修改，若要修改则需要转换成字典dict(zip(l1,l2))
版本：v1.0
"""
import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    # 出现的次数结果列表
    result_list = [0] * 11
    # 两个骰子的点数和列表
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    # zip 将对应的点数和次数关联起来
    for i in range(total_times):
        dice1 = roll_dice()
        dice2 = roll_dice()
        for j in range(2, 13):
            if dice1+dice2 == j:
                roll_dict[j] += 1
    for i, value in roll_dict.items():
        print('点数{}的次数是{},频率是{}'.format(i, value, value / total_times))


if __name__ == '__main__':
    main()
