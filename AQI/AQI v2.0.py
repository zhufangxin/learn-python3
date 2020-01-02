"""
功能：<读取>已经获取的json文件，并将前5的aqi数据<输出>到json文件
版本：v2.0
"""
import json


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
    top5_list = city_list[:5]
    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)  # 写到文件中
    f.close()


if __name__ == '__main__':
    main()
