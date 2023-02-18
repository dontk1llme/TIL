# boj 2606 바이러스
#1번 컴퓨터가 바이러스에 걸림...
#1번이랑 연결돼 있으면 count
#DFS ㄱㄱ

def dfs(start):
    global cnt
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1

N = int(input()) #컴퓨터의 수
C = int(input()) #연결되어 있는 컴퓨터의 수

graph = [[]*N for _ in range(N+1)] #+1: 컴터가 1부터라 그대로 사용하려고...
for i in range(C):
    a,b = map(int, input().split())
    graph[a].append(b) #양방향이라
    graph[b].append(a)

cnt = 0
visited = [0]*(N+1)
dfs(1)

print(cnt)