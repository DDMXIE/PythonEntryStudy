if __name__ == '__main__':

    # Python 访问字符串中的值
    # 语法格式： 变量[头下标:尾下标]
    string1 = 'Hello World!'
    string2 = "Runoob"
    print(string1[2:5])

    # 遍历字符串中的每一个元素
    for each in string1:
        print(each)

    # Python 字符串更新
    # 在python中，字符串是不可变对象，不能通过下标的方式直接赋值修改
    # string1[6] = "w"

    # 更新字符串
    print("已更新字符串 : ", string1[:6] + 'Runoob!')

    # 字符串连接
    str_new = string1 + string2
    print(str_new)

    # print字符串格式化
    print("我叫 %s 今年 %d 岁!" % ('小明', 10))

    # Python三引号
    # python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
    para_str = """这是一个多行字符串的实例
    多行字符串可以使用制表符
    TAB ( \t )。
    也可以使用换行符 [ \n ]。
    """
    print(para_str)

