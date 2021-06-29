# python_study
python 的学习



### 教程地址：

廖雪峰博客：https://www.liaoxuefeng.com/wiki/1016959663602400



### 基本数据类型：

| 类型      | 示例                                                         |
| --------- | ------------------------------------------------------------ |
| 字符串    | a = "hello" , b = 'hello', 使用 \ 转义                       |
| 整数      | a = 10                                                       |
| 浮点数    | a = 1.1                                                      |
| 布尔值    | a = True, b = False 大小写敏感                               |
| 列表/list | ['Michael', 'Bob', 'Tracy']，内部可以存放不同的类型，包括列表 |
|           |                                                              |

#### 字符串拼接，可以使用 '''xxxx''' 来做多行处理

```python
print('''n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \\'Adam\\''
    s3 = r'Hello, \"Bart\"'
    s4 = r\'\'\'Hello,
    Lisa!\'\'\''''
)
```

#### 赋值的一个例子

```python
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# result : ABC
# 原因是：a = "ABC" 是两个动作，首先申请 "ABC" 这个字符串，然后将变量 a 的指针指向这个字符串。当 b = a 的时候，b 的指针实际上是指向 ABC 这个字符串，而不是指向变量 a, 因此 a 的指向发生了变化后，不会影响b 的值
```

#### 常量的表示及除法

python 中没有常量，通常使用大写字母来表示常量，但是这个常量可以被修改

| 符号 | 示例                                                    |
| ---- | ------------------------------------------------------- |
| /    | 10 / 3 = 3.3333333   ;  9 / 3 = 3.0 。 返回结果是浮点数 |
| //   | 地板除，一定返回整数，可以理解为整除  10 // 3 = 3       |
| %    | 取模运算                                                |

### 字符编码及格式化

#### 字符编码

1. ASCII : 大小写字母，数字，无法表示中文，只占用一个字节
2. Unicode字符集：所有语言统一，全部都是用三个字节存储，占用大
3. UTF-8字符编码：英文等字符使用一个字节，中文等字符使用三个字节，节约且解决乱码问题

#### 格式化字符串

| 占位符 | 替换内容     |
| :----- | :----------- |
| %d     | 整数         |
| %f     | 浮点数       |
| %s     | 字符串       |
| %x     | 十六进制整数 |

1. 'Hi, %s, 你有%d个快递需要寄出，总费用在%f元' % ("小明",3, 3.14)
2. 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
3. % 如果存在字符串，可以使用 %% 转义s

### 列表集合

1. 可变列表（list）

   1. ```python
      # 定义方式：
      a = [1,3.14,False,"str",["a", "b"]]
      ```

   2. ```python
      # 获得长度：
      len(a)
      ```

   3. ```python
      # 通过坐标的方式进行访问，负数表示倒数
      a[1]
      a[-1]
      ```

   4. ```python
      # 新增
      a.append('b') # 新增到最后
      a.insert(7, 'c') # 新增到指定位置
      ```

   5. ```python
      # 移除
      a.pop()	# 移除最后一个元素
      a.pop(1) # 移除指定位置
      ```

2. 不可变列表（tuple）

   1. ```python
      # 定义方式
      # 元素不变，更加安全
      j = ("a", 123)
      j = () # 空元素
      j = (1, ) # 一个元素且是整数的时候，需要加上一个 ，   是为了防止被解释为数字
      ```

### 常用语法：

#### 	判断：

```python
height = 1.75
weight = 80.5
bmi = height / (weight * weight)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else :
    print("严重肥胖")
    
# elif == else if
```



#### 遍历：

```json
# 使用 for in 字符串|列表|元组|字典|集合：进行遍历

def traverseByFor(max):
    for x in list(range(max)):
        print("x : ", x)
    return

# 使用 while 的方式进行遍历
def traverseByWhile(max):
    i = 0
    while i < max:
        print("i : ", i)
        i += 1
    return
```



### dict 和 set:

#### dict 字典，类似map

```python
def getDict():
    d1 = {}
    d1["key1"] = 'value1'
    d1["key2"] = 2
    d1["key3"] = False
    print("key1 : ", d1["key1"])
    print("key2 : ", d1["key2"])
    print("key3 : ", d1["key3"])

    # 通过in判断是否存在key
    print("是否存在 key1 :", "key1" in d1)

    # 通过get判获取，不存在key也不会报错，返回 None
    print("获取 key3 :", d1.get("key3"))
    print("获取 key4 :", d1.get("key4"))

    # 通过 pop 移除某个键值对
    d1.pop("key3")
    print("获取 key3 :", d1.get("key3"))
```

#### set 和 Java 相同

```python
def getSet():
    # 无序，不能重复，创建的时候，需要使用一个list
    s1 = set(["key1", "key2", "key3", "key4"])
    print("set: ", s1)

    # 使用add来添加
    s1.add("key5")
    print("set: ", s1)

    # 使用remove来删除
    s1.remove("key1")
    print("set: ", s1)
```



### 函数：

#### 函数的参数数量及默认值：

```python
# 方法新增参数，新增参数支持默认值，允许不为空
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
    
if __name__ == '__main__':
    power(1);
    power2(1);  # 预期应该是3，使用了默认值2
    power2(1,3);    # 预期应该是4，填入了值
    power3(1, m=5); # 预期应该是 1+2+5 , n 使用默认值，m使用5
```

#### 可变参数：

```python
# 使用*num 来指定可变参数，这个*代表了可变参数，num 是 tuple 类型不可变
def addAll(*num):
    s = 0
    for x in num:
        s += x
    print(s)


if __name__ == '__main__':
    addAll(1, 2, 3, 4, 5) #随便填几个参数，都会被整合进一个 tuple

    list1 = [1, 2, 3, 4, 5, 6]
    addAll(*list1)        #已经存在的list or tuple ，可以在调用时，前面加上一个 *
```

#### 关键字参数：

```python
# 关键字参数：我把他理解为，传入的键值对，合并成一个dict，使用 **来标注入参
def dictParam(x, y, **kv):
    print("x=",x,"y=",y,"kv=",kv)
    
if __name__ == '__main__':
   
  dictParam("x","y", name='china',age="1")    # 输入内容为：x= x y= y kv= {'name': 'china', 'age': '1'}

    #也可以填入整个dict，使用 **
    dict1 = {"name":'abc',"age":2}
    dictParam("x1", "y1", **dict1)           # 输出内容：x= x1 y= y1 kv= {'name': 'abc', 'age': 2}
```







TODO [函数的参数 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888)