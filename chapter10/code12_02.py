class Car:
    color =""
    speed = 0
    
    # 생성자 함수
    #def __init__(self):
    #    self.color = "빨강"
    #    self.speed = 0
    # OR
    #def __init__(self, value1, value2):
    #    self.color = value1
    #    self.speed = value2
    #myCar1 = Car("빨강", 30); myCar2 = Car("파랑", 60)
    
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        
    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar2.color, myCar2.speed))

myCar3.upSpeed(160)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar3.color, myCar3.speed))