import time
import numpy as np

if __name__ == '__main__':
    list = []

    # 初始化list
    for i in range(0, 10000001):
        list.append(i)

    for_time_start = time.time()
    for each in list:
        print(each)
    for_time_end = time.time()

    it = iter(list)
    it_time_start = time.time()
    for x in it:
        print(x)
    it_time_end = time.time()

    np_list = np.array(list)
    flat_time_start = time.time()
    for i in np_list.flat:
        print(i)
    flat_time_end = time.time()
    print('for 循环运算时间：', for_time_end - for_time_start)
    print('iter 迭代运算时间：', it_time_end - it_time_start)
    print('flat 迭代运算时间：', flat_time_end - flat_time_start)


