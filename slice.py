#用切片实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    if s[:1]!=' ' and s[-1:]!=' ':
        return s
    elif s[:1]==' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

# 测试:
if trim('hello  ') != 'hello':
    print('trim(\'hello  \')，测试失败!')
elif trim('  hello') != 'hello':
    print('trim(\'  hello\')，测试失败!')
elif trim('  hello  ') != 'hello':
    print('trim(\'  hello  \')，测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('trim(\'  hello  world  \')，测试失败!')
elif trim('') != '':
    print('trim(\'\')，测试失败!')
elif trim('    ') != '':
    print('trim(\'    \')，测试失败!')
else:
    print('测试成功!')
