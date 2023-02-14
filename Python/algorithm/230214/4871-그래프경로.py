# [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로 (제출용) D2
# 인접행렬 사용

def dfs(start, end): #그냥dfs랑 똑같음
    stack = []
    visit = [0]*(V+1)
    stack.append(start)
    while stack:
        v = stack.pop()
        visit[v] = 1
        for t in range(V+1):
            if not visit[t]: #얘가 0이고
                if adjm[v][t]: #얘가 1이면 (연결되어 있으면)
                    stack.append(t)
    return visit[end]


T = int(input())
for tc in range(1, T+1):
    V,E=map(int, input().split()) #정점, 간선 개수
    adjm =  [[0] *(V+1) for _ in range(V+1)] #연결된 정점 표시
    for _ in range(E):
        x,y= map(int, input().split())
        adjm[x][y]=1
        # adjm[y][x]=1 #여기에서는 얘 안 해도 됨... 얘 하면 오류남. 근데 왜? 양방향 취급을 안해야만 하나봄

    result=1
    a,b=map(int, input().split())
    if not dfs(a,b):
        result = 0
    print(f'#{tc} {result}')
