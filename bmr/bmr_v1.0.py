"""
功能：计算基础代谢率BMR
版本：v1.0
"""


def main():
    print('请输入以下信息，用空格分割')
    input_str = input('性别 体重(kg) 身高(cm) 年龄:')
    str_list = input_str.split(' ')

    gender = str_list[0]
    print(type(gender))
    weight = float(str_list[1])
    height = float(str_list[2])
    age = int(str_list[3])

    if gender == '男':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (4.8 * age) + 655
    else:
        bmr = -1
    if bmr != -1:
        print('你的身高是{}cm，体重是{}kg, 年龄是{}'.format(height, weight, age))
        # print('你的身高是{0}cm，体重是{1}kg, 年龄是{2}'.format(height, weight, age)) #有顺序占位
        print('你的基础代谢率是{}'.format(bmr))
    else:
        print('请输入合法性别')


if __name__ == '__main__':
    main()
