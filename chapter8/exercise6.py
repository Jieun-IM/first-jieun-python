student_tuple = [('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'), ('211103', '김수정', '010-123-3333')]
# 1)
student = {}
for i in student_tuple:
    student[i[0]] = [i[1], i[2]]
for key, val in student.items():
    print(key, ':', val[0])
    
# 2)
s = input('학번을 입력하세요 : ')
for key, val in student.items():
    if s == key:
        print(s, '학생은', val[0]+'이며, 전화번호는', val[1]+'입니다.')