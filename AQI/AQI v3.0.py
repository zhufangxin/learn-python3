"""
功能：读取json文件，并转换成csv文件
Notes:
    csv:
    以行为单位
    以逗号分割每列数据，即使数据为空也要保留逗号
    csv.writerow(list)

版本：v2.0
"""

import json
import csv


def process_json_file(file_path):
    """
    解析json文件
    """
    f = open(file_path, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    file_path = input('请输入json文件名称：')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))
    f = open('aqi.csv', 'w', encoding='utf-8', newline='')  # 默认每行后加一行空行，newline=''指定末尾不加任何空行
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
