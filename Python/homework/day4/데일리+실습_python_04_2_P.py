students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

students.sort()
stnum=[]
count = 0
countnum = []


for i in students:
    if i not in stnum:
        stnum.append(i)

for i in stnum:
    for j in students:
        if i==j: count+=1
    countnum.append(count)
    count=0

semi_answer=[(stnum[i], countnum[i]) for i in range(0,len(stnum))]
semi_answer.sort(key=lambda x:-x[1])

answer = dict((x,y) for x,y in semi_answer)


print(f'최종: {answer}')

'''# 수형님코드.
dic = {}
for i in set(students):
    dic[i] = students.count(i)
l = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in l:
    print(i[0])
'''

