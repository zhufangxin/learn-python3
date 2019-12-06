# -*- coding: utf-8 -*-
"""
功能：汇率转换
版本： V5.0
新增功能:　1.程序结构化 2.简单函数的定义 Lamda  函数名=lamda <参数列表>:<表达式>
"""


# def convert_currency(im, rate):
#     """
#     汇率兑换函数
#     """
#     return im * rate


def main():
    """
    主函数
    """
    USD_VS_RMB = 6.77  # 固定值的命名用大写
    currency_inp_value = input('请输入带单位的货币金额(退出程序请输入Q):')
    unit = currency_inp_value[-3:]
    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB
    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        inp_money = eval(currency_inp_value[:-3])
        # 使用Lamda定义函数
        convert_currency2 = lambda x: x * exchange_rate

        # 调用函数
        # out_money = convert_currency(inp_money, exchange_rate)

        # 调用lamda函数
        out_money = convert_currency2(inp_money)
        print("转换后的金额为", out_money)


if __name__ == '__main__':  # ALWAYS RETURN TRUE
    main()
