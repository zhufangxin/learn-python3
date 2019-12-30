"""
功能：定义一个文件的工具类
版本：V6.0
知识点：面向对象编程(封装)
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


class FileTool:
    """
    文件工具类
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, line):
        f = open(self.file_path, 'a', encoding="utf-8")
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.file_path, 'r', encoding="utf-8")
        content = f.read()
        f.close()
        return content


def main():
    try_time = 5
    file_tool = FileTool('password.txt')

    while try_time > 0:
        strength_level = 0
        password = input('请输入密码：')

        password_tool = PasswordTool(password)
        password_tool.process_password()

        file_tool.write_to_file('密码:{}, 强度:{}\n'.format(password, password_tool.strength_level))
        content = file_tool.read_from_file()
        print(content)

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
