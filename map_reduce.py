#map(func,iterable): map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#reduce(func,iterable)把fn的结果继续和序列的下一个元素做累积计算

#练习1: 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
    return name.lower().title()
 
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#练习2: Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def multiply(x,y):
	return x*y
def prod(L):
    return reduce(multiply,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('pass!')
else:
    print('fail!')

#练习3: 用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def fn(x,y):
	return x*10+y
def str2float(s):
	n= s.index('.')
	L1=list(map(int,list(s[:n]))) #list(s[:n])->[x for x in s[:n]]
	L2=list(map(int,list(s[n+1:]))) #[x for x in s[n+1:]]
	return reduce(fn,L1)+reduce(fn,L2)/10**len(L2)
	 
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('pass!')
else:
    print('fail')
