def dfs(n):
    global ans
    # 가지치기: n회, lst를 이미 해봤다면 다시 처리 필요 없음(중복 제거)
    # 튜플로 변환해서 v[]에 표시 => 600mS
    # if (n, int("".join(lst))) in v:     # 이미 처리한적 있음
    #     return
    # v.append((n, int("".join(lst))))

    # 한 개의 숫자로 변환 (v에서 해당 정수값을 찾는데 O(N)) => 200mS
    # if (n + int("".join(lst))*100) in v:     # 이미 처리한적 있음
    #     return
    # v.append(n + int("".join(lst))*100)

    # 한 개의 숫자로 변환 (dct에서 해당 정수값을 찾는데 O(1)) => 150mS
    if (n + int("".join(lst)) * 100) in dct:  # 이미 처리한적 있음
        return
    dct[n + int("".join(lst)) * 100] = 1

    if n == N:
        # 리스트(문자열이 요소)를 정수로 변환해서 정답 갱신
        ans = max(ans, int("".join(lst)))
        return

    # L개에서 2개 뽑는 모드 조합
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(n + 1)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for test_case in range(1, T + 1):
    st, N = input().split()
    N = int(N)
    lst = [ch for ch in st]
    L = len(lst)
    v = []  # 중복 체크를 위한 배열
    dct = {}

    ans = 0
    dfs(0)
    print(f'#{test_case} {ans}')