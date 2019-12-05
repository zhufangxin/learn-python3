# -*- coding: utf-8 -*-
"""
功能：汇率转换
版本： V3.0
新增功能:　程序一直运行，直到用户选择退出
"""

USD_VS_RMB = 6.77  # 固定值的命名用大写
currency_inp_value = input('请输入带单位的货币金额(退出程序请输入Q):')
while currency_inp_value != 'Q':
    unit = currency_inp_value[-3:]
    if unit == 'CNY':
        rmb_inp_value = currency_inp_value[:-3]
        rmb_value = eval(rmb_inp_value)
        usd_amt = rmb_value / USD_VS_RMB
        print('USD amount is: ', usd_amt)
    elif unit == 'USD':
        usd_inp_value = currency_inp_value[:-3]
        usd_value = eval(usd_inp_value)
        cny_amt = usd_value * USD_VS_RMB
        print('CNY amount is: ', cny_amt)
    else:
        print('This currency unit is not supported.')
    print('*****************************************')
    currency_inp_value = input('请输入带单位的货币金额(退出程序请输入Q):')
print('程序已退出')