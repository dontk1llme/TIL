# 11724 연결 요소의 개수
# DFS

def dfs(start, depth):
    visited[start]=True
    for i in arr[start]:
        if not visited[i]:
            dfs(i, depth+1)

N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]

#그래프
for i in range(M):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0]*(N+1)
count = 0

for i in range(1,N+1):
    if not visited[i]: # 방문 안햇으면
        if not arr[i]: # 연결된 그래프가 없으면
            count+=1 #개수 +1
            visited[i]=True
        else: #연결된 그래프가 있으면
            dfs(i,0)
            count+=1

print(count)