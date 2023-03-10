import turtle

import random

 

## 전역 변수 부분 ##

swidth, sheight = 500, 500

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6

shapeList= []

playerTurtles = [] #거북이 2차원 리스트

 

## 메인 함수 부분 ##

if __name__ == "__main__" :

    turtle.title('거북이 리스트 활용')

    turtle.shape('turtle')

    turtle.setup(width = swidth + 50, height = sheight + 50)

    turtle.screensize(swidth, sheight)

 

    shapeList = turtle.getshapes()  ## getshapes() : 현재 사용 가능한 모든 거북이 모양의 이름 목록을 반환

    for i in range(1, 100) :

        random.shuffle(shapeList)   ## shuffle(shapeList) : shapeList항목을 섞어놓는 함수

        myTurtle = turtle.Turtle(shapeList[0])

        tX = random.randrange(-swidth / 2, swidth / 2)

        tY = random.randrange(-sheight / 2, sheight / 2)

        r = random.random(); g = random.random(); b = random.random()

        tSize = random.randrange(1, 3)

        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])  ## append() : 리스트 맨 뒤에 항목을 추가

 

    for tList in playerTurtles :

        myTurtle = tList[0]

        myTurtle.color((tList[4],tList[5],tList[6]))

        myTurtle.pencolor((tList[4],tList[5],tList[6]))

        myTurtle.turtlesize(tList[3])

        myTurtle.goto(tList[1], tList[2])

 

turtle.done()