#  [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 (제출용) D2
# https://velog.io/@ase0574/5102.-%ED%8C%8C%EC%9D%B4%EC%8D%AC-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EA%B8%B0%EB%B3%B8-6%EC%9D%BC%EC%B0%A8-%EB%85%B8%EB%93%9C%EC%9D%98-%EA%B1%B0%EB%A6%AC

def bfs(S,G):
    q = [S]
    visited[S]=1
    while q:
        t = q.pop(0)
        if t == G:
            print(f'#{tc} {result[t]}')
            return
        #이어진 노드들 찾기
        for j in range(V+1):
            if graph[t][j]==1 and visited[j]==0:
                q.append(j)
                #간선 저장
                result[j] = result[t]+1
                visited[j]=1
    if result[G]:
        print(f'#{tc} {result[G]}')
    else:
        print(f'#{tc} 0')

T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    S,G = map(int, input().split())

    #간선 그래프
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        start = lst[i][0]
        end = lst[i][1]
        graph[start][end]=1
        graph[end][start]=1
    visited=[0 for _ in range(V+1)]
    result = [0 for _ in range(V+1)]
    bfs(S,G)