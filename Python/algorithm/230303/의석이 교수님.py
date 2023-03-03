T = int(input())
for test_case in range(1, T + 1):
    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            # if j < len(arr[i]):
            try:
                ans += arr[i][j]
            except:
                pass
    print(f'#{test_case} {ans}')