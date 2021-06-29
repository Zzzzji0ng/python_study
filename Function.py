def multiReturn():
    a = 1
    b = 2
    c = False
    return a, b, c
    # 可以返回多个，实际上返回的是一个


# 普通方法
def power(x):
    print(x)

# 加了一个参数
def power1(x, n):
    print(x + n)

# 如果方法新增了一个参数，那么之前的调用者会抛出异常
# 这里可以使用一个特性，多出来的参数可以提供默认值，当n不存在的时候，n默认为2
def power2(x, n = 2):
    print(x + n)

def power3(x, n = 2, m = 3):
    print(x + n + m)

# 使用*num 来指定可变参数，这个*代表了可变参数，num 是 tuple 类型不可变
def addAll(*num):
    s = 0
    for x in num:
        s += x
    print(s)

# 关键字参数：我把他理解为，传入的键值对，合并成一个dict，使用 **来标注入参
def dictParam(x, y, **kv):
    print("x=",x,"y=",y,"kv=",kv)

if __name__ == '__main__':
    # a, b, c = multiReturn()
    # print("a :", a)
    # print("b :", b)
    # print("c :", c)

    # power(1);
    # power2(1);  # 预期应该是3，使用了默认值2
    # power2(1,3);    # 预期应该是4，填入了值
    # power3(1, m=5); # 预期应该是 1+2+5 , n 使用默认值，m使用5

    # addAll(1, 2, 3, 4, 5) #随便填几个参数，都会被整合进一个 tuple

    # list1 = [1, 2, 3, 4, 5, 6]
    # addAll(*list1)        #已经存在的list or tuple ，可以在调用时，前面加上一个 *

    dictParam("x","y", name='china',age="1")    # 输入内容为：x= x y= y kv= {'name': 'china', 'age': '1'}

    #也可以填入整个dict，使用 **
    dict1 = {"name":'abc',"age":2}
    dictParam("x1", "y1", **dict1)           # 输出内容：x= x1 y= y1 kv= {'name': 'abc', 'age': 2}