import numpy as np

if __name__ == '__main__':

    # 将Python array_like对象转换为Numpy数组
    list1 = [1, 2, 3, 4, 5]
    np_list1 = np.array(list1)
    print(np_list1)
    print(type(np_list1))

    # Numpy创建矩阵
    col = 4
    index = 3
    graph = np.matrix([[0] * col] * index)
    print(graph)

    # Numpy原生数组的创建
    # zeros(shape)将创建一个用指定形状用0填充的数组。默认的dtype是float64。
    list_val0 = np.zeros((2, 3))    # 创建两行三列的二维数组
    print(list_val0)

    # ones(shape)将创建一个用1个值填充的数组。它在所有其他方面与zeros相同。
    list_val1 = np.ones((1, 10))    # 创建长度为10的一维数组
    print(list_val1)

    # 创建有规律递增的数组
    # 创建从0开始步增为1的到9为止的数组
    np_list2 = np.arange(10)
    print(np_list2)
    # 创建从2开始到9的步增为1的数组
    np_list3 = np.arange(2, 10)
    print(np_list3)
    # 创建从2开始到2.9步增为0.1的数组
    np_list4 = np.arange(2, 3, 0.1)
    print(np_list4)

