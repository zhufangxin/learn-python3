"""
功能：保存密码及强度到文件中
版本：V4.0
知识点：读文件
"""


def main():
    f = open('password.txt', 'r', encoding='UTF-8')
    # 1. read()　返回整个文件内容
    # print(f.read())

    # 2. readline() 返回文件下一行内容
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    # 3. readlines() 返回整个文件内容的列表，每项是以换行符为结尾的一行字符串
    for line in f.readlines():  # same:  for line in f
        print(line)

    f.close()

if __name__ == '__main__':
    main()
