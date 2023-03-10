## 거북이 그래픽으로 숫자 입력받아 다각형 그리기 ##
import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리시겠어요?(3~6): "))

for i in range(n):
    t.forward(100)
    t.left(360//n)
    
turtle.done()