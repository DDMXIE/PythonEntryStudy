import numpy as np

if __name__ == '__main__':
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([2.0, 2.0, 2.0])
    a = a + 1
    print(a)

    # 当 a 与 b 长度相同时，可以进行对应元素的加减乘除操作
    print(a * b)
    print(a + b)
    print(a - b)
    print(a / b)

    # reshape构造
    x = np.arange(4)
    print(x)
    xx = x.reshape(4, 1)
    print(xx)
    # 二维相加广播
    print(xx + x)