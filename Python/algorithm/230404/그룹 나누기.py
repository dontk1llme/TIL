#  5248 [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 (제출용) D2
# find_set과 union을 사용하는 문제 -> https://bingbing-study.tistory.com/100

# find_set: x를 포함하는 집합 찾기
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    man = list(range(1, N + 1))
    want = list(map(int, input().split()))

    # 출석번호 인덱스까지 parent 리스트 만들기 (0번은 사용 x)
    parent = [i for i in range(N + 1)]

    # 짝지어서 union
    for i in range(0, len(want), 2):
        union(want[i], want[i + 1])

    ans = set()
    for i in range(1, N + 1):
        ans.add(find_set(i))
    print(f'#{tc} {len(ans)}')
