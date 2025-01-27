#STOP SIGN CODE
import turtle

stop = turtle.Turtle()
stop.shape('arrow')

distance = 120
sides = 8
# Choose color and use angles to determine how many turns the turtle will make
angle = 360 / sides
colores = "red"


stop.penup()
stop.goto(-75, 100)
stop.pendown()
stop.color(colores)
stop.begin_fill()
# repeat for all sides of octagon
for i in range(sides):
   stop.forward(distance)
   stop.right(angle)

stop.end_fill()
stop.hideturtle()
#write Stop inside of the stop sign
stop.goto(-135,-30)
stop.penup()
stop.right(90)
stop.forward(60)
stop.color('white')
stop.write('STOP',font = ("Cambria", 100, "bold"))
