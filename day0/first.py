from turtle import *

speed(15)
width(5)

# walls
color("pink")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# door
forward(80)

color("orange")
begin_fill()

left(90)
forward(60)

right(90)
forward(40)

right(90)
forward(60)

end_fill()

# left window
penup()
goto(20,100)
pendown()

color("yellow")
begin_fill()

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

end_fill()

# right window
penup()
goto(180,100)
pendown()

color("yellow")
begin_fill()

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

end_fill()

#roof
penup()
goto(0,200)
pendown()

color("pink")
begin_fill()

left(120)
forward(120)

right(60)
forward(114)

end_fill()

exitonclick()



