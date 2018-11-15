'''# PythonDraw.py
import turtle
# 窗体的位置、大小
turtle.setup(650, 350, 200, 200)
# turtle.goto(x,y) 使海龟到达(x,y)
# turtle.penup()的别名turtle.pu() 将画笔抬起
turtle.penup()
# 向海龟正前方运行 别名turtle.forward(d)
turtle.fd(-250)
# turtle.bk(x) 向海龟正后方运行
# turtle.pendown()的别名turtle.pendown() 将画笔落下
turtle.pendown()
# turtle.pensize(width)的别名turtle.width(width) 设置画笔宽度
turtle.pensize(25)
# 修改画笔颜色 color可以是颜色字符串、rgb值 turtle.pencolor(0.63,0.13,0.94) turtle.pencolor((0.63,0.13,0.94))
turtle.pencolor("purple")
# turtle.seth(angle)别名turtle.setheading(angle)改变当前海龟的行进角度 angle为绝对度数
# turtle.left(angle) turtle.right(angle)使海龟向左或向右转动angle
turtle.seth(-40)
# range(n) 产生从0到n-1的整数序列
# range(m,n) 产生从m到n-1的整数序列
for i in range(4):
    # turtle.circle(r,extent)根据半径r绘制extent角度的弧形，圆心在海龟左侧r距离的点
    # 以海龟当前位置左侧的某个点为圆心进行曲线运行
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
# 运行完之后不会退出
turtle.done()
# turtle.colormode(mode), mode=1.0使用小数值、mode=255使用整数值'''
import turtle
turtle.penup()
turtle.bk(45)
turtle.pendown()
for i in range(9):
    turtle.fd(95)
    turtle.left(80)

turtle.done()