dic = {'one':'하나', 'two':'둘', 'house':'집', 'Korea':'한국'}

print('사전 프로그램 시작... 종료는 q를 입력')
for i, j in dic.items():
    print('$ '+'< '+ i+':'+j)
    




while True:
    user_input = input('$ > ' )

    if user_input in dic:
        print(dic.get(user_input))
    elif user_input == 'q':
        print('사전을 종료합니다')
        break
    elif user_input not in dic:
        print(user_input+'이(가) 사전에 없습니다.')
    