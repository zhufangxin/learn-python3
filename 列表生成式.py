#通过添加if语句保证列表生成式能正确地执行#
#isinstance函数可以判断变量是否是某类型
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if  isinstance(i,str) ==True]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('pass')
else:
    print('fail')