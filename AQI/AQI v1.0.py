"""
功能：AQI空气质量计算
版本：v1.0
"""


def call_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_value(pm_value):
    if 0 <= pm_value < 36:
        iaqi = call_linear(0, 50, 0, 35, pm_value)
    elif 36 <= pm_value < 76:
        iaqi = call_linear(50, 100, 35, 75, pm_value)
    elif 76 <= pm_value < 116:
        iaqi = call_linear(100, 150, 75, 115, pm_value)
    else:
        pass
    return iaqi


def cal_co_value(co_value):
    global iaqi
    if 0 <= co_value < 3:
        iaqi = call_linear(0, 50, 0, 2, co_value)
    elif 3 <= co_value < 5:
        iaqi = call_linear(50, 100, 2, 4, co_value)
    elif 5 <= co_value < 14:
        iaqi = call_linear(100, 150, 4, 14, co_value)
    else:
        pass
    return iaqi


def cal_aqi(cal_list):
    pm_value = cal_list[0]
    co_value = cal_list[1]
    pm_aqi = cal_pm_value(pm_value)
    co_aqi = cal_co_value(co_value)
    result_list = []
    result_list.append(pm_aqi)
    result_list.append(co_aqi)
    return result_list


def main():
    print('请输入以下值（用空格分开）')
    str_input = input('(1)PM2.5: (2)CO:')
    str_value = str_input.split(' ')
    pm_value = float(str_value[0])
    co_value = float(str_value[1])
    cal_list = []
    cal_list.append(pm_value)
    cal_list.append(co_value)
    aqi_result_list = cal_aqi(cal_list)
    aqi = max(aqi_result_list)
    print('空气质量为{}'.format(aqi))


if __name__ == '__main__':
    main()
