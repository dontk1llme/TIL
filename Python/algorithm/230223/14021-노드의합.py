# [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 (제출용) D3

T = int(input())
for tc in range(1, T+1):
    N,M,L = map(int, input().split())

    #완전이진트리에 데이터 저장
    tree = [0]*(N+1)
    for _ in range(M):
        idx, d = map(int, input().split())
        tree[idx] = d

    #루프
    for n in range(N, L-1, -1):
        tree[n//2]+=tree[n] #부모노드에 자식노드값 누적
    ans = tree[L]
    print(f'#{tc} {ans}')




