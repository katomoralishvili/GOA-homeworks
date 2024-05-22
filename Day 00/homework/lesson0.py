print("day 0 homework")
from turtle import *

#we want to paint a house


#step 1: draw a square
speed(10)
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a window
begin_fill()
penup()
goto(0,70)
pendown()
left(120)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
#drawaing a second window
penup()
goto(200,70)
pendown()
begin_fill()
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

#end of drawing a house





exitonclick()