def multiReturn():
    a = 1
    b = 2
    c = False
    return a, b, c
    # 可以返回多个，实际上返回的是一个

if __name__ == '__main__':
    a, b, c = multiReturn()
    print("a :", a)
    print("b :", b)
    print("c :", c)
