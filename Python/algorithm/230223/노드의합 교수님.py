def postord(n):
    if 1 <= n <= N:  # 존재하는 노드!
        if tree[n] == 0:  # 현재노드 계산필요
            tree[n] = postord(n * 2) + postord(n * 2 + 1)
        return tree[n]
    return 0  # 존재하지 않는 노드=>0리턴
    # 모든경로에서 반드시 리턴!!


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # [1] 완전이진트리에 데이터 저장
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, d = map(int, input().split())
        tree[idx] = d

    # [2] 순회(post-order)
    # ans = postord(L)

    # [3] 루프로처리
    for n in range(N, L - 1, -1):
        tree[n // 2] += tree[n]  # 부모노드에 자식노드 값 누적
    ans = tree[L]
    print(f'#{tc} {ans}')