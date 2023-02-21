T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] q에 순서대로 N개의 피자 채움
    q = []
    for i in range(1, N + 1):
        q.append((i, lst.pop(0)))

    # [2] q에서 데이터를 꺼내는경우 순서대로 append
    while q:
        n, piz = q.pop(0)  # 피자번호, 치즈량
        piz = piz // 2  # 치즈량 반으로 감소
        if piz == 0:
            if lst:
                i += 1
                q.append((i, lst.pop(0)))  # 대기하고 있는 미조리 피자 순서대로 넣음
        else:
            q.append((n, piz))  # 다시 큐에 넣음
    ans = n
    print(f'#{tc} {ans}')