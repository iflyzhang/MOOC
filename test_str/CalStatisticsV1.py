'''
基本统计值计算
'''

def getnum():
    '''获取不确定数量的多个数据'''
    nums=[]
    iNumStr = input("输入数字（回车退出）:")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("输入数字（回车退出）:")
    return nums

def mean(numbers):
    '''平均值'''
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers,mean):
    '''方差'''
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1),0.5)

def median(numbers):
    '''中位数'''
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2 - 1] + new[size//2])/2
    else:
        med = new[size//2]
    return med

n = getnum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}".format(m,dev(n,m),median(n)))
