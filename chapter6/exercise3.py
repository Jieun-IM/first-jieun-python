def max3(n1, n2, n3):
    result = n1 if n1 > n2 else n2
    result = result if result > n3 else n3
    return result
    
def min3(n1, n2, n3):
    result = n1 if n1 < n2 else n2
    result = result if result < n3 else n3
    return result     
 
n = input('3 수를 입력하시오 : ').split()

print('가장 큰 수:', max3(int(n[0]), int(n[1]), int(n[2])))
print('가장 작은 수:', min3(int(n[0]), int(n[1]), int(n[2])))