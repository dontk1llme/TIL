T = int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split())
    arr = list(map(int, input().split()))
    max = 0
    min = 10000*N
    for i in range(0, N-M+1):
        sum = 0
        for j in range(i, M+i):
            sum += arr[j]
        if sum > max: max = sum
        if sum < min: min = sum
    print(f'#{tc} {max-min}')


# 이렇게 하면 런타임 에러 날 수도 있음 (데이터 다 더해서 비교하니까 시간이 길어요)
# 해결법: 1-4 더하면 다음 2-5를 다 더하는 게 아니라 1-4에서 2-4까지는 가져오고 5만 더해주기
# 그러면 루프가 줄어용 아래 코드!!
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#     sm = 0
#     for i in range(M):
#         sm += lst[i]
#     mn = mx = sm        # mn, mx값 초기화 필요
#     for i in range(M, N):
#         sm += lst[i]    # i위치 값 추가
#         sm -= lst[i-M]  # i-M 위치 값 제거
#         if mx<sm:
#             mx=sm
#         if mn>sm:
#             mn=sm
#     print(f'#{test_case} {mx-mn}')