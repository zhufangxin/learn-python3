"""
功能：模拟掷两个骰子，可视化投掷结果
知识点:　Numpy 科学计算
版本：v5.0
"""
import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def main():
    total_times = 100
    roll1_list = np.random.randint(1, 7, 1000)
    roll2_list = np.random.randint(1, 7, 1000)
    roll_list = roll1_list + roll2_list
    # 输出直方图的统计结果
    hist, bins = np.histogram(roll_list, bins=range(2, 14))

    # 绘制直方图
    plt.hist(roll_list, bins=range(2, 14), edgecolor='black', linewidth=1, alpha=0.75, density=1, rwidth=0.8)
    # 设置x轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5  # 坐标位置
    plt.xticks(tick_pos, tick_labels)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
