"""
递归　绘制分形树
"""
import turtle


def draw_branch(branch_length):
    """
    绘制分形树
    """
    if branch_length > 5:
        # 　绘制右侧树枝
        turtle.forward(branch_length)
        print('向前', branch_length)
        turtle.right(20)
        print('向右20度')
        draw_branch(branch_length - 15)
        # 　绘制左侧树枝
        turtle.left(40)
        print('向左40度')
        draw_branch(branch_length - 15)
        #   返回之前的树枝
        turtle.right(20)
        print('向右20度')
        turtle.backward(branch_length)
        print('向后', branch_length)


def main():
    """
    主函数
    """
    turtle.left(90)
    draw_branch(40)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
