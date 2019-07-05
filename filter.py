#filter
#filter(func,iterable)把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

#练习: 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

def is_palindrome(n):
	nn=str(n)
	return nn==nn[::-1]

	
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('pass')
else:
    print('fail')	