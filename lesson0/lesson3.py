from turtle import *

#we want to paint a house


#step 1: draw a square
speed(10)
width(7)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
#end of square

#step 2: drawing a door
begin_fill()
penup()
goto(40,0)
pendown()
left(90)
forward(45)
right(90)
forward(20)
right(90)
forward(45)
end_fill()


#step 3: drawing a roof
penup()
goto(0,100)
pendown()
begin_fill()
right(45)
backward(70)
left(90)
forward(70)
end_fill()
penup()
goto(0,40)
pendown()



#step 4:drawing a window
begin_fill()
left(45)
forward(25)
left(90)
forward(30)
left(90)
forward(25)
end_fill()
penup()
goto(100,40)
pendown()
  

#step 5:drawing a second window 
begin_fill()
forward(25)
right(90)
forward(30)
right(90)
forward(25)
end_fill()
penup()
goto(200,0)
pendown()

#we want to draw another house

#step 1: draw a square
forward(90)
left(90)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
penup()
goto(235,0)
pendown()

#step 2: drawing a door
begin_fill()
backward(45)
left(90)
forward(25)
right(90)
forward(45)
end_fill()
penup()
goto(200,90)
pendown()

#step 3: draw a roof
begin_fill()
left(125)
forward(60)
right(75)
forward(55)
end_fill()
penup()
goto(200,30)
pendown()
#step 4: draw a window
begin_fill()
left(40)
forward(20)
left(90)
forward(15)
left(90)
forward(20)
end_fill()
penup()
goto(290,30)
pendown()
#step 5: draw a second window
begin_fill()
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()
penup()
goto(-100,0)
pendown()
#we want to draw another house next to first one

#step 1: draw a square
penup()
goto(-155,0)
pendown()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
penup()
goto(-120,0)
pendown()

#step 2: draw a door
begin_fill()
right(180)
forward(60)
right(90)
forward(35)
right(90)
forward(60)
end_fill()
penup()
goto(-155,100)
pendown()

#step 3: draw a roof
begin_fill()
left(125)
forward(65)
right(75)
forward(60)
end_fill()
penup()
goto(-150,30)
pendown()

#step 4: draw a window
begin_fill()
left(40)
forward(20)
left(90)
forward(20)
left(90)
forward(25)
end_fill()
penup()
goto(-55,30)
pendown()

#step 5: draw another window
begin_fill()
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()
penup()
goto(-300,-100)
pendown()

#draw a tree
begin_fill()
color("brown")
left(90)
forward(150)
right(90)
forward(30)
right(90)
forward(150)
right(90)
forward(30)
end_fill()
penup()
goto(-300,0)
pendown()
color("green")
begin_fill()
right(90)
forward(0)
left(90)
forward(30)
right(90)
forward(40)
left(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
left(90)
forward(40)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(40)
left(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
left(90)
forward(40)
right(90)
forward(40)
end_fill()


#we want to draw a sun

penup()
goto(-350,350)
color("yellow")
begin_fill()
pendown()
circle(70)
end_fill()