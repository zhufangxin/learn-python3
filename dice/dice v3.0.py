"""
功能：模拟掷两个骰子，可视化投掷结果
知识点:　matplotlib绘制散点图
版本：v1.0
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100
    # 出现的次数结果列表
    result_list = [0] * 11
    # 两个骰子的点数和列表
    roll_list = list(range(2, 13))
    # zip 将对应的点数和次数关联起来
    roll_dict = dict(zip(roll_list, result_list))
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        dice1 = roll_dice()
        dice2 = roll_dice()
        roll1_list.append(dice1)
        roll2_list.append(dice2)

        for j in range(2, 13):
            if dice1 + dice2 == j:
                roll_dict[j] += 1
    for i, value in roll_dict.items():
        print('点数{}的次数是{},频率是{}'.format(i, value, value / total_times))

    # 绘制散点图
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
