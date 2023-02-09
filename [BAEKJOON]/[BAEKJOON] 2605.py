#BOJ 2605 줄세우기

N = int(input())
student=list(map(int,input().split()))
newstd = [] #줄세울 배열

for i in range(1,N+1):
    newstd.append(i) #1,2,3,4,5 순서대로 append할 거임

    #첫 순서는 무조건 맨 앞이니까 제외하고 나머지만 -> if로 고려하려고 했는데 어차피 0임.
    time = student[len(newstd)-1] #인덱스는 len보다 하나 작으니까
    l = len(newstd)-1 #인덱스는 len보다 하나 작으니까
    for j in range(time): #입력받은 횟수만큼
        newstd[l],newstd[l-1]=newstd[l-1],newstd[l] #뒤에서 앞에거 바꿈
        l-=1
    
for k in range(N):
    print(newstd[k], end=' ')

