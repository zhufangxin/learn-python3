"""
功能：根据输入的文件判断是json格式还是csv格式，并进行相应的读取操作
Notes:
    1.csv.reader() 将每行记录作为列表返回
    2.使用with操作文件对象，不管处理文件过程中是否发生异常，都能保证关闭文件，不需要close()语句
    3.os模块
"""

import json
import csv
import os


def process_json_file(file_path):
    """
    解析json文件
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        city_list = json.load(f)
        print(city_list)


def process_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))


def main():
    file_path = input('请输入json文件名:')
    file_name, file_ext = os.path.splitext(file_path)
    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('不支持的文件格式')


if __name__ == '__main__':
    main()
