#탐색이랑 백트래킹이랑 연결짓지 않기

T = int(input())

def dfs(s):
    # 방문표시, 첫 방문 시 처리할 일 있으면 여기에서 하기
    v[s] = 1
    alst.append(s)

    for e in adj[s]:#연결된 노드(미방문시
        if v[e]==0: #미방문시
            dfs(e)

for tc in range(1, T+1):
    V,E = map(int,input().split())
    #무가중치 양방향
    adj = [[] for _ in range(V+1)] #0번째 인덱스는 안씀
    for _ in range(E):
        s,e = map(int, input().split())
        adj[s].append(e) #양방향 연결
        adj[e].append(s)

    #여러개 연결 시 낮은 번호부터 방문 -> 오름차순 정렬 필수
    for i in range(1, V+1):
        adj[i].sort() #안에 항목들 하나하나 정렬

    v = [0]*(V+1)
    alst = [] #방문 순서
    dfs(1)


    print(f'#{tc}', *alst)


