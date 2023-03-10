import turtle
import random

turtle.shape('turtle')
turtle.width(3)
count = 0

while True:
    a = random.randrange(2)
    if a == 0:
        turtle.right(90)
        turtle.forward(50)
    else :
        turtle.left(90)
        turtle.forward(50)
    
    count += 1
    if count == 10:
        turtle.done()