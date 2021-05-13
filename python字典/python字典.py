if __name__ == '__main__':
    # 初始化字典
    dict = {'a': 1, 'b': 2, 'c': '3'}

    # 通过key值访问value值
    print("dict['b']")
    print(dict['b'])

    # 修改字典
    dict['b'] = 'this is b'
    print(dict)

    # 删除字典里的元素
    # 删除键值对
    # del dict['b']
    # print(dict)

    # 清空字典
    # dict.clear()
    # print(dict)

    # 删除整个字典
    # del dict
    # print(dict)

    # 字典的特性
    # 1-不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
    dict_animal = {1: 'monkey', 2: 'fish', 3: 'rabbit', 3: 'snake', 4: 'horse'}
    print(dict_animal[3])  # 3为重复的键，后者覆盖前者

    # 2-键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
    # dict_2 = {['Name']: 'Runoob', 'Age': 7}
    # print("dict['Name']: ", dict_2['Name'])

    # 字典的遍历
    for each in dict_animal:
        print(each)     # 遍历所有的键
        print(dict_animal[each])    # 遍历所有的值

    # 将所有值放进一个值的list
    val_list = []
    val_list = list(dict_animal.values())
    print(val_list)

    # 元组字典的遍历
    dict_tup = {(1, 2), (2, 8), (3, 7), (4, 5), (6, 15), (7, 11)}
    key_tup_list = []
    value_tup_list = []
    for each in dict_tup:       # 注意是无序遍历 因为python 中字典是hash存储
        print(each)
        key_tup_list.append(each[0])
        value_tup_list.append(each[1])
    print(key_tup_list)
    print(value_tup_list)


