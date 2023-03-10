from tkinter import N


def max_and_min(n1, n2, n3):
    max = n1 if n1 > n2 else n2
    max = max if max > n3 else n3
    
    min = n1 if n1 < n2 else n2
    min = min if min < n3 else n3
    return max, min
    
n = input('3 수를 입력하시오 : ').split()
max, min = max_and_min(int(n[0]), int(n[1]), int(n[2]))
print('가장 큰 수 :', max)
print('가장 작은 수 : ', min)