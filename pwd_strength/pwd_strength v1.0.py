"""
功能：判断密码强度
版本：V1.0
"""


def check_number_exist(password):
    # 判断字符串中是否有数字
    for c in password:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password):
    # 判断字符串中是否有字母
    for c in password:
        if c.isalpha():
            return True
    return False


def main():
    password = input('请输入密码：')
    strength_level = 0
    # １.密码长度是否大于８
    if len(password) > 8:
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

    if strength_level == 3:
        print('密码强度合格')
    else:
        print('密码强度不合格')


if __name__ == '__main__':
    main()
