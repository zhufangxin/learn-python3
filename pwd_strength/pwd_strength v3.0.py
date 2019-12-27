"""
功能：保存密码及强度到文件中
版本：V3.0
知识点：写文件
步骤：打开文件　操作文件　关闭文件

"""


def check_number_exist(password):
    # 判断字符串中是否有数字
    has_number = False
    for c in password:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password):
    # 判断字符串中是否有字母
    has_alpha = False
    for c in password:
        if c.isalpha():
            has_alpha = True
            break
    return has_alpha


def main():
    try_time = 5
    while try_time > 0:
        strength_level = 0
        password = input('请输入密码：')

        # １.密码长度是否大于等于８
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度至少８位')
        # 2.是否包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码需要包含数字')
        # 3.判断字符串中是否有字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码需要包含字母')

        f = open('password.txt', 'a', encoding="utf-8")  # w:覆盖　a:在末尾追加  # 默认文件路径和py文件相同
        f.write('密码:{}, 强度:{}\n'.format(password, strength_level))
        f.close()

        if strength_level == 3:
            print('密码强度合格')
            break
        else:
            try_time -= 1
            print('密码强度不合格!')

    if try_time == 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
