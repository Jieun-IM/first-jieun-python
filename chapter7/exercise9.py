def overlap(A, B):
    n = 0
    lap = False
    for i in range(0, len(A)):
        if B.startswith(A[n: len(A)]):
            result = A[0:n] + B
            lap = True
            break
        n += 1
    if lap == False:
        result = A + B
    return result

A = input('문자열 A : ')
B = input('문자열 B : ')

C = overlap(A, B)
print(C)