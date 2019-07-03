#使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L!=[]:
        max=L[0]
        min=L[0]
        for i in L:
            if i>max:
                max=i
            if i<min:
                min=i
        return (min,max)
    else:
        return  (None, None)


# 测试:
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
