'''汉诺塔  递归'''
count = 0
def hanoi(n,src,dst,mid):
    '''

    :param n: 圆盘个数
    :param src: 原柱子
    :param dist: 目标柱子
    :param mid: 中间柱子
    :return:
    '''
    global count
    if n == 1:
        print("{}:{}->{}".format(n,src,dst))
        count += 1

    else:
        # 将n-1个圆盘从src搬到mid
        hanoi(n-1,src,mid,dst)
        # 将最后一个圆盘从src搬到dst
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        # 将n-1个圆盘从mid搬到dst
        hanoi(n - 1, mid, dst,src)
hanoi(3,'A','C','B')
print('移动次数：{}'.format(count))