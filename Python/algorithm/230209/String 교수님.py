#첫번째
T = 10
for test_case in range(1, T + 1):
    _ = input()
    st1 = input()
    st2 = input()
    M, N = len(st1), len(st2)
    ans = 0

    for i in range(N - M + 1):
        # # [1] 문자열 자체를 비교
        # if st1 == st2[i:i+M]:
        #     ans += 1
        # [2] 각 요소를 비교
        for j in range(M):
            if st1[j] != st2[i + j]:  # 하나라도 다르면 break
                break
        else:  # 모두 같은 경우(break 하지 않음)
            ans += 1

    print(f'#{test_case} {ans}')


#두번째
T = 10
for test_case in range(1, T + 1):
    _ = input()
    st1 = input()
    st2 = input()
    M, N = len(st1), len(st2)
    ans = 0

    for i in range(N - M + 1):
        if st1 == st2[i:i + M]:
            ans += 1

    print(f'#{test_case} {ans}')