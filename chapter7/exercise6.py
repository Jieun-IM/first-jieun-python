
s = input('문자열을 입력하세요 : ')
for i in range(len(s) + 1):
    print(s[0:i])
for j in range(-1,-len(s), -1):
    print(s[0:j])