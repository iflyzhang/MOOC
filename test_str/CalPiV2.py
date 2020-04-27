'''
工程思维：蒙特卡罗方法计算圆周率
抽象一个过程，用计算机自动化求解
'''
from random import random
from time import perf_counter

DARTS = 1000*1000*10# 当前区域抛撒点的总数
hits = 0.0 # 撒在圆内的点的数量
start = perf_counter() # 计时
for i in range(1,DARTS):
    x,y = random(),random()# 随机生成两个0~1的坐标值
    dist = pow(x ** 2 + y ** 2,0.5)# 计算点到圆心的距离
    if dist <= 1.0:
        hits = hits + 1
    pi = 4 * (hits/DARTS)
print("圆周率：{}".format(pi))
print("运行时间为：{:.5f}".format(perf_counter()-start))
