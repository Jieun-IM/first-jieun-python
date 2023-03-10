n = int(input('n을 입력하시오 : '))

snake = []
num = 1
for i in range(0, n):
    innerSnake = []
    for j in range(num, num+n):
        innerSnake.append(j)
    if i % 2 != 0:
        innerSnake.sort(reverse=True)
    snake.append(innerSnake)
    num += n
    
for i in range(0, n):
    for j in range(0, n):
        print(snake[i][j], end="  ")
    print()
    