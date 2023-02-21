'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v, N):
    visited = [0] * (N+1) # visited 생성
    q = [v]# 큐 생성 # 시작점 인큐
    visited[v]=1 # 시작점 인큐표시
    while q:
        t = q.pop(0) #디큐
        print(t, end=' ') #t에서 처리할 일
        for i in adjl[t]:  # t에 인접이고 방문한 적 없는 v
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[t]+1 #v 인큐되엇음 표시
    print() #얘 없으면 다 한줄에나와서 에러

T =int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2) #양방향
        adjl[n2].append(n1)

    print(f'#{tc}', end=' ')
    bfs(1,V) #시작정점 1, 마지막 정점 V