"""

# 使用def 定义方法
def add1(x, y):
    return x + y
print(add1(1, 1))


# 参数中可以指定默认值
def add2(x, y = 2):
    return x + y
# 一个会按照输出参数
print(add2(1, 3))
# 另一个没填的会按照默认值注入
print(add2(1))
# 参数可以不按照定义顺序填入，但是需要指定参数的名称
print(add2(y=3, x=2))



# 使用#开头的参数，表示可变参数，会被判定为tuple
def add3(*args):
    s = 0
    for item in args:
        s += item
    return s

print(add3(1, 2, 3))
print(add3(1, 2, 3, 4))
print(add3(1, 2, 3, 4, 5))




# 使用 import .. as .. 来引入其他模块，
import module2 as m2
m2.sayWord()

# 使用 from .. import ... 来引入其他模块的某个函数
from module2 import sayWord
sayWord()

# 使用 from ... import ... 来引入其他包的某个模块
from module import module3
module3.sayWord()


# 作用域
def foo():
    b = 'hello'  # 局部作用域, 一个定义在函数中的局部变量, 函数外部不能访问，对于 bar(), 他是嵌套作用域

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100  # 全局作用域，因为它没有定义在任何一个函数中，全局可以访问

    # print(b)  # NameError: name 'b' is not defined
    foo()

"""

def foo():
    a = 100
    print(a)

if __name__ == '__main__':
    a = 200
    foo()
    print(a)
    # 输出结果还是200，内外的a不是同一个a了，而是一个局部变量