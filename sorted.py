#sorted()
#对list进行排序,它还可以接收一个key函数来实现自定义的排序,key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序. sorted([36, 5, -12, 9, -21], key=abs) >>>[5, 9, -12, -21, 36]

#练习1: 假设我们用一组tuple表示学生名字和成绩： L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], 请用sorted()对上述列表分别按名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)	

#练习2: 再按成绩从高到低排序
def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
