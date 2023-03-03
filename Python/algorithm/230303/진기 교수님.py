T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = 'Possible'
    for t in sorted(lst):
        cnt += 1
        if cnt > (t // M) * K:  # 도착한 사람수 > 만들어진 붕어빵수
            ans = 'Impossible'
            break

    print(f'#{test_case} {ans}')