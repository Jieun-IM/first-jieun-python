class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print(self.width, '가로의 선이 제거되었습니다.')
        print(self.height, '세로의 선이 제거되었습니다.')
r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])
