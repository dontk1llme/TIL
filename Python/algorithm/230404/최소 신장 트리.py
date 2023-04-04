# [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 (제출용) D4

#MST
def find_set(x): #x가 속한 집합의 대표 원소 출력
    while rep[x]!=x: #x==rep[x]가 될 때까지
        x = rep[x]
    return x

def union(x,y): #y의 대표원소가 x의 대표원소를 가리키도ㅗㄱ
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V,E = map(int,input().split())
    rep = [i for i in range(V+1)]
    graph = [] #저장
    for _ in range(E):
        v1, v2, w = map(int,input().split()) #정점, 정점, 가중치
        graph.append([v1, v2, w])

    #가중치 기준 오름차순 정렬
    graph.sort(key=lambda x:x[2])
    # print(graph)

    #N개 정점 (V+1), N-1개의 간선 선택
    N = V+1
    s= 0 #MST에 포함된 간선의 가중치 합
    cnt = 0
    MST = [] #선택된 애들만 저장
    for u,v,w in graph: #가중치가 작은 것부터
        if find_set(u) != find_set(v): #사이클이 생기지 않으면
            cnt+=1
            s+=w #가중치 합 구함
            MST.append([u,v,w])
            union(u,v) #사이클 만들어버려
            if cnt==N-1: #MSt 구성 완료
                break
    print(f'#{tc} {s}')
