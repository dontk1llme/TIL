# [BAEKJOON] 2669 직사각형 네개의 합집합의 면적 구하기

lst = [list(map(int, input().split())) for _ in range(4)]
graph = [[0]*101 for _ in range(101)] #그림

for i in lst:
    for j in range(i[0],i[2]):
        for k in range(i[1],i[3]):
            graph[j][k]=1

ans = 0
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] !=0:
            ans+=1

print(ans)