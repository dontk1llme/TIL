T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # [2] 출력할 대상 값만 리스트로 만들어서 계산
    # [1] 모두 1인 삼각형 모양 arr생성
    arr = [[1]*(i+1) for i in range(N)]
    for i in range(2, N):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)
 
#---------------------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*(N+1) for _ in range(N+1)]
    # 문제 설명대로의 구현
    arr[1][1] = 1       # [1] 첫 줄은 항상 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            # [2] 한 행 위 왼쪽과 한 행위 값의 합
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
 
    print(f'#{test_case}')
    # 모두 출력이 아닌, 0이 아닌 값만 출력(또는 범위)
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(f'{arr[i][j]}', end=' ')
        print()

