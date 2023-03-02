# BOJ 1240 - 노드사이의 거리
#튜플 활용하면 간선정보 쉽게 활용 가능함
#https://jie0025.tistory.com/152

from collections import deque

def bfs(start, find):
    q = deque()
    q.append((start,0)) #시작노드, 거리0
    visited = [0]*(N+1)
    visited[start]=1

    while q:
        v,d = q.popleft()
        if v==find: #찾는 노드와 번호가 일치하면 거리 리턴
            return d
        for i,l in graph[v]: #연관된 노드 번호와 거리
            if not visited[i]:
                visited[i]=1
                q.append((i,d+l)) #지금까지 노드를 찾으며 거리 기록


N,M= map(int,input().split()) #N개의 노드 트리
graph = [[] for _ in range(N+1)]

for _ in range(N-1): #트리 생성
    n1,n2,l = map(int, input().split())
    graph[n1].append((n2,l))
    graph[n2].append((n1,l))
for _ in range(M): #거리 찾을 애들
    n1,n2 = map(int, input().split())
    print(bfs(n1,n2))

