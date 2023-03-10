import turtle

t = turtle.Turtle()

t.shape("turtle")

t.width(3)
t.shapesize(3, 3)

while True :
    command = input("명령을 입력하시오: ")
    
    if command == "f" :
        t.forward(100)
    if command == "h" :
        t.shapesize(10, 10)
    if command == "n" :
        t.shapesize(3, 3)
    a = int(input("1~9 사이의 값을 입력하시오: "))
    print(a)
    if a :
        t.shapesize(a, a)
    