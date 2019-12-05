# -*- coding: utf-8 -*-
"""
功能：汇率转换
版本： V1.0
"""

# 汇率
USD_VS_RMB = 6.77  # 固定值的命名用大写
rmb_inp_value = input('please enter the amount of RMB:')  # return string
rmb_value = eval(rmb_inp_value)  # eval: convert string to number
usd_amt = rmb_value / USD_VS_RMB
print('USD amount is: ', usd_amt)
