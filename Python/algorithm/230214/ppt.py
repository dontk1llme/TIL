T = int(input())
for tc in range(1, T+1):
    #입력
    V,E = map(int, input().split())
    #인접행렬 생성
    mat = [[0] * (V+1) for _ in range(V+1)] 
    #노드별 인접행렬 리스트
    adjL = [[] for _ in range(V+1)]
    #입력받는 두 값 인접행렬에 1 삽입
    for i in range(E):
        a,b=map(int, input().split())
        mat[a][b]=1
        mat[b][a]=1

        adjL[a].append(b)
        adjL[b].append(a)
    

    
    print(adjL)


# 1
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7