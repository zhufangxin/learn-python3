"""
功能：定义一个password的工具类
版本：V5.0
知识点：面向对象编程
"""


class PasswordTool:
    """
    密码工具类
    """

    def __init__(self, password):  # 外部传入password
        # 类的属性
        self.password = password  # 将外部属性传递给本身
        self.strength_level = 0

    # 类的方法
    def process_password(self):
        # １.密码长度是否大于等于８
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少８位')
        # 2.是否包含数字
        if self.check_number_exist():  # 默认传入self
            self.strength_level += 1
        else:
            print('密码需要包含数字')
        # 3.判断字符串中是否有字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码需要包含字母')

    def check_number_exist(self):
        # 判断字符串中是否有数字
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        # 判断字符串中是否有字母
        has_alpha = False
        for c in self.password:
            if c.isalpha():
                has_alpha = True
                break
        return has_alpha


def main():
    try_time = 5
    while try_time > 0:
        strength_level = 0
        password = input('请输入密码：')

        password_tool = PasswordTool(password)
        password_tool.process_password()
        f = open('password.txt', 'a', encoding="utf-8")  # w:覆盖　a:在末尾追加  # 默认文件路径和py文件相同
        f.write('密码:{}, 强度:{}\n'.format(password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print('密码强度合格')
            break
        else:
            try_time -= 1
            print('密码强度不合格!')

    if try_time == 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
