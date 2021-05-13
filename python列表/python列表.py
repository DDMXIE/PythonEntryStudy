if __name__ == '__main__':
    list = ['red', 'green', 'blue', 'yellow', 'white', 'black']

    # 访问列表中的值
    # 第一个元素下标为0
    a = list[2]
    print(a)

    # 遍历访问
    # for each in list:
    #     print(each)

    # 反向索引访问
    # 最后一个元素的索引为 -1，往前一位为 -2
    b = list[-2]
    print(b)

    # 反向索引遍历
    count = -1
    for i in range(0, len(list)):
        print(list[count])
        count = count - 1

    # 可以使用方括号 [] 的形式截取字符，如下所示
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    # 从第一位（包含）开始截取到第五位（不包含）
    new_nums = nums[1:5]
    print(new_nums)

    # 同样，可以用负数索引值截取
    list_2 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
    # 读取第二位
    print("list_2[1]: ", list_2[1])
    # 从第二位开始（包含）截取到倒数第二位（不包含）
    print("list_2[1:-2]: ", list_2[1:-2])

    # 更新列表
    list = ['Google', 'Runoob', 1997, 2000]
    print("第三个元素为 : ", list[2])
    list[2] = 2001
    print("更新后的第三个元素为 : ", list[2])

    list1 = ['Google', 'Runoob', 'Taobao']
    list1.append('Baidu')
    print("更新后的列表 : ", list1)

    # 删除列表元素
    # 可以使用 del 语句来删除列表的的元素，如下实例：
    print('原始列表 :', list)
    del list[2]
    print('当前列表 :', list)


