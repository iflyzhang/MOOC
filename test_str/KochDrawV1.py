import turtle as t

def koch(size,n):
    '''
    科赫曲线绘制
    :param size: 每个直线长度
    :param n: 阶数
    :return:
    '''
    if n == 0:
        t.fd(size)
    else:
        # [0,60,-120,60]旋转角度
        for angle in [0,90,270,270,90]:
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(800,400)# 窗体大小
    t.penup()
    t.goto(-300,-50)
    t.pendown()
    t.pensize(2)
    koch(600,3)
    t.hideturtle()

def snowMain():
    t.setup(600,600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(2)
    level = 3 # 3阶科赫雪花
    koch(400,level)
    t.right(120)
    koch(400, level)
    t.right(120)
    koch(400, level)
    t.hideturtle()

# snowMain()



main()