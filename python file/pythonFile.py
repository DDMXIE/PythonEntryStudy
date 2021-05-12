
if __name__ == '__main__':
    # 打开所需文件并初始化文件对象
    fp = open(file='./file dic test/test1.txt', mode='r')

    # 读文件
    # print(fp.read())

    # mode :
    #       r:读文件
    #       w:重新写
    #       a+:接续写
    fp2 = open(file='./file dic test/test1.txt', mode='a+')
    string = 'hello tony '
    fp2.write(string)
    fp2.close()

    # 再次阅读写好的文件 注：写好的文件一定要先关闭再重新阅读
    print(open(file='./file dic test/test1.txt', mode='r').read())