import sys
import time
from time import sleep
from tqdm import tqdm

# python 进度条实现代码    普通进度条
def progress_bar_1(total):
     for i in range(1, int(total)):
         print("\r", end="")
         print("total {}: ".format(i), "▋" * (i // 2), end="")
         sys.stdout.flush()
         # time.sleep(0.05)

# python 进度条实现代码    任务型进度条
def progress_bar_2(total):
    for i in tqdm(range(0, total)):
        # 模拟你的任务
        sleep(0.00001)
    # sleep(0.5)

# python 进度条实现代码    普适进度条
def progress_bar_3(total):
    for i in range(0, total):
        print("▋", end="")
        if i % 100 == 0 and i != 0:
            print('\n')

if __name__ == '__main__':
    # progress_bar_1(10001)
    # progress_bar_2(10001)
    progress_bar_3(201)