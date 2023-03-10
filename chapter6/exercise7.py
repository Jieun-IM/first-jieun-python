# 재귀함수 사용 X
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i        
    return result

print(factorial(5))
print(factorial(7))
print(factorial(10))

# 재귀함수 사용 O
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(7))
print(factorial(10))