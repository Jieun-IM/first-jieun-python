fruits_dic = {'사과':0, '배':0, '수박':0, '귤':0, '포도':0}
fruits_dic['사과'], fruits_dic['배'], fruits_dic['수박'], fruits_dic['귤'], fruits_dic['포도'] = input('사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ').split()

print()
print('------------- 오늘의 과일 가격 -------------')
for key in fruits_dic.keys():
    print(key, ':', fruits_dic[key], '원')
    
KEY = input('구매를 원하는 과일의 이름을 입력하시오 : ')
print('오늘의', KEY, '가격은', fruits_dic[KEY], '원 입니다.')