#闭包
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#练习:利用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    print('outer')
    f=[0]
    def counter():
        print('inner')
        f[0]=1+f[0]
        return f[0]  #用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('pass!')
else:
    print('fail!')
	
	
#闭包外-- 闭包内-- 闭包内-- 闭包内-- 闭包内-- 闭包内-- 1 2 3 4 5
#同一个返回函数对象，重复执行的时候，仅跑函数内的内容。返回函数外的内容是跑1次
#假如是这么写：
#def counter():
#    print('闭包中--')
#    f[0] = f[0] + 1
#    return f
#print是等内容全部执行完，再输出的。
##[5] [5] [5] [5] [5]