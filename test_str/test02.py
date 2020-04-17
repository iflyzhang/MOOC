#TextProBarV1.Py
'''
time库使用
单行动态刷新
'''
import time
sca1e = 50
print("执行开始".center(sca1e//2,'-'))
start = time.perf_counter()
for i in range(sca1e + 1):
    a = '*' * i
    b ='.'* (sca1e - i)
    c = (i/sca1e)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')# \r 在打印输出前，光标退回当前行行首
    time. sleep(0.1)
print("\n" + "执行结束".center(sca1e//2,'-'))
