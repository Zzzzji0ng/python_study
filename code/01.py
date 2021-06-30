"""
示例
"""


"""
a = 1
b = 1.1
c = False
d = "str"
e = 1 + 1j
print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
print(type(c))   # <class 'bool'>
print(type(d))   # <class 'str'>
print(type(e))   # <class 'complex'>
"""





"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
"""
x = int(input("x = "))
y = 0
if x > 1:
    y = 3 * x - 5
elif x <= 1 or x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print("f(%d) = %d" % (x, y))
"""





"""

# range() 方法，是获取一个范围的list
# range(x, y), 获取从 x - y 的list,不包括y
# range(x, y, z) 获取x - y中，以z递增或递减

# 使用for 循环来遍历
for x in range(0, 10):
    print(x)

for x in range(0, 10, 2):
    print(x)

# 使用 while 来遍历
x = 10
while x > 0:
    print("x = %d" % x)
    x = x - 1
    
"""