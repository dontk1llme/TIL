# [BAEKJOON] 3985 롤 케이크

L = int(input()) #롤 케이크 길이
N = int(input()) #방청객의 수
cake = [-1]*L
lst = [list(map(int, input().split())) for _ in range(N)] #종이에 적어낸 수
will = []
real = 0

for i in lst:
    for j in range(i[0],i[1]+1):
        will.append((lst.index(i),i[1]-i[0]))
        if cake[j] == -1:
            cake[j]=lst.index(i)
        else:
            break

#예상
will = sorted(will, key=lambda x:(-x[1],x[0])) #두번째인자 내림차, 첫인자 오름차
print(will[0][0]+1) #인덱스니까

#실제
newcake = []
for i in range(N):
    newcake.append([i,0]) #튜플인 것처럼 만들어서 append
for i in range(len(cake)):
    if cake[i]!=-1: #-1(임시값)이 아니고
        for j in newcake:
            if j[0]==cake[i]: #케이크에 넣은 값과 같으면 +1
                j[1]+=1

newcake = sorted(newcake, key = lambda x:(-x[1],x[0]))
print(newcake[0][0]+1)




