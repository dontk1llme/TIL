# 1683. 데일리실습 3-4.
# 복합 자료형인 딕셔너리 작성 및 활용
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

type = ['A','B','AB','O']
ls = [0]*4

#count
for i in blood_types:
    if i == type[0]: ls[0]+=1
    elif i == type[1]: ls[1]+=1
    elif i == type[2]: ls[2]+=1
    elif i == type[3]: ls[3]+=1

#make dict
dc = {}
for i in range(0,4):
    dc[type[i]] = ls[i]

print(dc)