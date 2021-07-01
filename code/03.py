# 字符串
def str():
    # 定义方式
    str1 = 'hello'
    str2 = "hello"
    str3 = """
    hello
    world
    多行使用三个"包裹
    """
    str4 = "\"这里使用了转义字符，结果中会有一个\""
    str5 = r"\"在字符串开头加上一个r，\\就无法使用转移字符"

    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)

    # 字符串的常用操作
    str6 = "this is test text"
    # 长度
    print(len(str6))
    # 是否包含
    print("is contain : ", "text" in str6)
    # 获取某个字段的下标
    print("is 在第几个：", str6.find("is"))
    # 格式化输出
    print("%d * %d = %d" % (1, 2, 1 * 2))
    print("{0} * {1} = {2}".format(2, 3, 2 * 3))

    # 字符串切片
    # [indexStart, indexEnd, size]  起点坐标，重点坐标，步长（需要和方向正负一致）
    print(str6[1:2])
    print(str6[2:10:2])
    print(str6[::2])

# 列表
def list():
    # 如何定义list
    list1 = [1, 2, 3, 4, 5]
    list2 = range(0, 10)
    print(list1)
    print(list2)

    # 常用操作
    # 获取长度
    print(len(list1))
    print(len(list2))

    #获取某个位置的值
    print(list1[1])
    # print(list1[5]) 会抛出越界异常
    print(list1[-1])    #取最后一个

    #添加元素
    #添加到尾部
    list1.append(6)
    #添加到指定坐标
    list1.insert(0, -1)
    #把某个元素删除
    list1.remove(5)
    #根据坐标删除
    list1.pop(1)
    print(list1)

    # 遍历的方式
    for x in list2:
        print(x)

    list3 = sorted(list2, reverse=True)
    for x in list3:
        print(x)

# 元组 tuple
def tuple():
    # 定义方式
    tuple1 = {1, 2, 3, 4, 5}
    for x in tuple1:
        print(x)

    # 元组是不可改变的，更加节省内存，适合多线程的情况下使用

# 字典 dict
def dict():
    # 定义方式
    dict1 = {"name":"name1", "age":21, "money": 5}
    print(dict1)

    #取值
    print(dict1["name"])
    print(dict1.get("money"))

    #更新
    dict1["name"] = "name2"
    dict1.update(money=10)
    print(dict1["name"])
    print(dict1["money"])

    #删除
    dict1.pop("money")
    print(dict1.get("money"))


    #遍历
    for key in dict1:
        print("%s : %s" % (key, dict1[key]))




if __name__ == '__main__':
    # str()
    # list()
    # tuple()
    dict()