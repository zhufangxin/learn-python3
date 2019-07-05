#迭代器 Iterator
#凡是可作用于for循环的对象都是Iterable类型(1.如list、tuple、dict、set、str等 2.generator)
#用isinstance()判断一个对象是否是Iterable/Iterator对象
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
