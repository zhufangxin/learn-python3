"""
功能：模拟掷两个骰子，可视化投掷结果
知识点:　matplotlib绘制直方图
        直方图：显示各分组的频率或数量分布情况
        plt.hist(数据列表data，分组边界bins)
版本：v1.0
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100
    roll_list = []

    for i in range(total_times):
        dice1 = roll_dice()
        dice2 = roll_dice()
        roll_list.append(dice1 + dice2)

    # 绘制散点图
    plt.hist(roll_list, bins=range(2, 14), edgecolor='black', linewidth=1, alpha=0.75, density=1)
    plt.title = '骰子点数统计'
    # plt.xlabel = '点数'
    # plt.ylabel = '频率'
    plt.show()


if __name__ == '__main__':
    main()
