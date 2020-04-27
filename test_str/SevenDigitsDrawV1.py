'''绘制七段数码管V1'''
import turtle

def drawLine(draw):
    '''画一条线'''
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)

def drawDigit(digit):
    '''根据参数digit决定绘制的图案'''
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)#第一条线
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)# 回到起点后左转
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)#掉头
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(40) #绘制完一个数码管后，起点向前移动一段距离

def drawDate(date):
    for i in date:
        drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20200419')
    turtle.hideturtle()
    turtle.done()
main()