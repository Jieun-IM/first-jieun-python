student_tup = (('211101', '조성훈', '010-1234-4500'), ('211102', '김은지', '010-2230-6540'), ('211103', '윤소정', '010-3232-7788'))
# 1)
student = {}
for i in student_tup:
    student[i[0]] = [i[1], i[2]]

print('학생의 정보 목록')
for key, val in student.items():
    print({key: val})
    
# 2)    
number = input('학번을 입력하시오 : ')
for key, val in student.items():
    if number == key:
        print('이름 :', val[0])
        print('연락처 :', val[1])
        
# 3)
print()
grade = [4.3, 3.9, 4.25]
n = 0
for key in student.keys():
    student[key].append(grade[n])
    n += 1
print('학생의 정보 목록')
for key, val in student.items():
    print({key: val})
    
# 4)
result = 0
for val in student.values():
    result += float(val[2])
print('전체 학생의 학점 평균 %.2f' % (result/3.0))