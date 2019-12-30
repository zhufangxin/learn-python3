"""
功能：模拟掷骰子
知识点:random, enumerate
版本：v1.0
"""
import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    # 统计值列表　
    # 初始化列表[0,0,0,0,0,0]
    total_times = 10
    result_list = [0] * 6
    for i in range(total_times):
        dice = roll_dice()
        for j in range(1, 7):
            if dice == j:
                result_list[j - 1] += 1
    for i, value in enumerate(result_list):
        print('点数{}的次数是{},频率是{}'.format(i + 1, value, value / total_times))


if __name__ == '__main__':
    main()
