from turtle import *
import colorsys

header_text = "te quiero mucho muchito"
color("purple") 
penup()
goto(-100, 250) 
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

speed(20)
bgcolor("sky blue")
h = 0

penup()
goto(-90, 10)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  
        h += 0.010
        rt(90)
        circle(150 - j * 6, 100)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

penup()
goto(-103, 103)
pendown()
color("brown")
begin_fill()
circle(50)  
end_fill()
done() 