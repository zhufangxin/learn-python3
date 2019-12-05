# -*- coding: utf-8 -*-
"""
功能：汇率转换
版本： V4.0
新增功能:　函数应用 计算转换后金额
"""


def convert_currency(im, rate):
    """
    汇率兑换函数
    """
    return im * rate

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
    out_money = convert_currency(inp_money, exchange_rate)
    print("转换后的金额为", out_money)
