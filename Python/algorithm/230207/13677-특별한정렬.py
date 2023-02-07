T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    newarr = [0]*10

    #우선 전부다 정렬하고!
    for i in range(N - 1, 0, -1):  # 각 구간의 끝
        for j in range(i):  # 비교할 왼쪽 원소
            if arr[j] > arr[j + 1]:  # > 말고 < 하면 내림차순으로 가능
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 큰 원소 오른쪽으로 (오름차)

    #10개만 정렬하니까
    tenarr = arr[:5] + arr[-5:]

    # 내림차: 인덱스 1부터 2씩
    n=9
    for i in range(0,9,2):
        newarr[i]=tenarr[n]
        n-=1

    # 오름차: 인덱스 끝부터 -2씩
    for i in range(9,0,-2):
        newarr[i]=tenarr[n]
        n-=1

    print(f'#{tc}', end=' ')
    print(*newarr)


    #교수님코드
    #모두 정렬하고 갖다붙이면 그순간 시간초과! -> selection sort
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     N = int(input())
    #     lst = list(map(int, input().split()))
    #
    #     # seletcion sort를 부분적으로만 (10개) 진행
    #     for i in range(10):  # 정렬할 개수 10개(0~9)
    #         idx = i
    #         for j in range(i + 1, N):
    #             if i % 2 == 0:  # 짝수=> 큰 값 순서
    #                 if lst[idx] < lst[j]:
    #                     idx = j
    #             else:  # 홀수=> 작은 값 순서
    #                 if lst[idx] > lst[j]:
    #                     idx = j
    #         lst[i], lst[idx] = lst[idx], lst[i]
    #     print(f'#{test_case}', *lst[:10])
