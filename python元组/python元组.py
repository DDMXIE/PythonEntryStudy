if __name__ == '__main__':
    # 已有元组
    tup1 = ('physics', 'chemistry', 1997, 2000)

    # 访问元组1:    通过for循环访问
    for each in tup1:
        print(each)

    # 访问元组2:    通过下标访问
    print("tup1[0]: ", tup1[0])

    # 访问元组3:    根据范围访问
    print(print("tup1[1]-tup1[3]: ", tup1[1:4]))

    # 修改元组1:    元组拼接
    tup2 = (12, 34.56)
    tup3 = ('abc', 'xyz')
    tup_tpl = tup2 + tup3
    print(tup_tpl)

    # 修改元组2:    覆盖修改
