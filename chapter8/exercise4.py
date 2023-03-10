lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]
# 1)
count = {}
for i in range(10, 51, 10):
    count[i] = lst.count(i)
unique = []
for key, val in count.items():
    if val == 1:
        unique.append(key)
print('중복이 없는 원소 : ', unique)

# 2)
once = set(lst)
print('전체 원소 : ', sorted(list(once)))

# 3)
for key, val in count.items():
    if val > 1:
        print(key, ':', val, '회')