import turtle as t

t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
# 获取数据
datals = []
with open('./test_data/data.txt') as f:
    for line in f:
        line = line.replace("\n","")
        datals.append(list(map(eval,line.split(','))))
# 自动绘制
for i in range(len(datals)):
    '''
    300,1,144,0,1,0
    行进距离,转向判断（0坐，1右）,转向角度,RGB三个颜色通道
    '''
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])