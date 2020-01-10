"""
功能：根据输入的城市，从网页上获取对应的aqi
Notes:
    1.HTTP
      requests: get()/post()
                status_code/text

"""

import requests


def get_html_text(url):
    r = requests.get(url, timeout=30)
    return r.text


def main():
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    html_text = get_html_text(url)

    aqi_div = """<div class="span12 data">
        <div class="span1">
          <div class="value">
            """
    index = html_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = html_text[begin_index:end_index]
    print('{}的aqi是{}'.format(city_pinyin, aqi_val))


if __name__ == '__main__':
    main()
