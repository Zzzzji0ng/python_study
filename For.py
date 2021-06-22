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

if __name__ == '__main__':
    # traverseByFor(100)
    traverseByWhile(100)


