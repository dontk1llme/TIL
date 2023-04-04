# kruskal
# 링크 중심! 굉장히 명료함!
# prim보다는 추천

def find_set(n):
    if n == p[n]:
        return n
    p[n] = find_set(p[n])
    return p[n]


def union(s, e):
    p[find_set(e)] = find_set(s)


def kruskal():
    # [1] 링크중심의 처리: w값 오름차순으로 정렬=>짧은 가중치값 부터 처리
    arr.sort(key=lambda x: x[2])

    # [3] v개의 링크를 선택(같은 그룹이 아닌 경우에만 선택)
    cnt = ret = 0
    for (s, e, w) in arr:
        # s, e가 연결되어 있는 않은 경우(사이클이 아닌경우) 선택
        if find_set(s) != find_set(e):
            union(s, e)
            ret += w
            cnt += 1
            if cnt == V:  # 노드개수-1 개를 연결하면 종료
                return ret
    # 이 코드가 실행되지는 않겠지만...
    return -1


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    # [1] make_set(): 각자 자기가 대표인 그룹생성
    p = [n for n in range(V + 1)]

    ans = kruskal()
    print(f'#{test_case} {ans}')



# prim
# 노드 중심!
def prim(ss):
    v[ss] = 1
    ret = 0

    for _ in range(V):  # 전체노드 - 1개 만큼 반복처리
        mn, i_min = INF, 0
        for s in range(V + 1):
            if v[s] == 1:  # [1] MST에 포함된 노드를 하나씩 처리
                # 포함 안 된 노드중 최소비용 연결 노드 찾기
                for e in range(V + 1):
                    if v[e] == 0 and mn > adj[s][e]:
                        mn, i_min = adj[s][e], e

        v[i_min] = 1
        ret += mn

    return ret


INF = 10 * 1001
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[INF] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = adj[e][s] = w
    v = [0] * (V + 1)

    ans = prim(0)
    print(f'#{test_case} {ans}')