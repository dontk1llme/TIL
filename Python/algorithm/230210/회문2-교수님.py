def isPal(arr, M):
    for lst in arr:
        for i in range(N - M + 1):
            # [2] 인덱스로 절반만 비교
            for j in range(M // 2):
                if lst[i + j] != lst[i + M - 1 - j]:
                    break
            else:  # break 안 한 경우=> 모두 같음!
                return True
            # [1] 슬라이싱 사용
            # if lst[i:i+M]==lst[i:i+M][::-1]:
            #     return True

    return False


T = 10
for test_case in range(1, T + 1):
    _ = input()
    N = 100
    arr = [input() for _ in range(N)]
    arr_t = list(zip(*arr))
    for M in range(N, 1, -1):
        if isPal(arr, M) or isPal(arr_t, M):
            break
    else:
        M = 1
    print(f'#{test_case} {M}')

#-----------------------
def isPal(arr, M):
    for lst in arr:
        for i in range(N - M + 1):
            # [2] 인덱스로 절반만 비교
            for j in range(M // 2):
                if lst[i + j] != lst[i + M - 1 - j]:
                    break
            else:  # break 안 한 경우=> 모두 같음!
                return True
            # [1] 슬라이싱 사용
            # if lst[i:i+M]==lst[i:i+M][::-1]:
            #     return True

    return False


T = 10
for test_case in range(1, T + 1):
    _ = input()
    N = 100
    arr = [input() for _ in range(N)]
    # arr_t = list(zip(*arr))   # tuple 또는 list
    arr_t = ["".join(x) for x in zip(*arr)]  # arr와 동일 구조로 만들어서 사용

    for M in range(N, 1, -1):
        if isPal(arr, M) or isPal(arr_t, M):
            break
    else:
        M = 1
    print(f'#{test_case} {M}')