x, y = (input("x, y의 값을 입력하시오: ")).split()
x = int(x)
y = int(y)

def square(i, j):
    print(i)
    k = i ** 2
    l = j ** 2
    return k, l

x_sq, y_sq = square(x, y)


print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))