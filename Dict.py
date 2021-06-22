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


if __name__ == '__main__':
    getSet()


