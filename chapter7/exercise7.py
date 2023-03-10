fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

for i in fruit_list:
    print(f'{i} : 문자열의 길이 {len(i)}')



max = 0
for i in fruit_list:
    max = max if max > len(i) else len(i)
    
max_list = []
for i in fruit_list:
    if len(i) == max:
        max_list.append(i)
    
for i in max_list:
    fruit_list.remove(i)

    
print('가장 길이가 긴 문자열 :',max_list[0]+', '+ max_list[1])
print(fruit_list)