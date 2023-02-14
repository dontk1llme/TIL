# Stack1_연습문제_2: 깊이우선탐색 (제출용) D3
# 스택으로 하래.........
# 모르겟어서 교수님풀이 기다릴래.........

# https://data-marketing-bk.tistory.com/44

def dfs(graph):
    visited = []
    stack = [1]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack+=sorted(list(graph[node]-set(visited)), reverse=True)
            #스택은 뒤부터 나가니까 역순으로 정렬한대...

    return visited


T = int(input())
for tc in range(1, T+1):
    #입력
    V,E = map(int, input().split())
    #인접행렬 생성
    mat = [[0] * (V+1) for _ in range(V+1)] 
    #입력받는 두 값 인접행렬에 1 삽입
    for i in range(E):
        a,b=map(int, input().split())
        mat[a].append(b)
        mat[b].append(a)

    for i in list(dfs(mat)):
        print(i, end=' ')
    # print(visit_list)
    # print(mat)