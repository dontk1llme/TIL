# 5688. 세제곱근을 찾아라 D3
# 타임에러........................ -> 이분탐색으로 해야댄대요
# 근데 아래 코드대로 해서 어케 답이 나오는지가 넘 신기한데?............ 이해안댐 아직

#코드 1
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    s, e = 1, N
    ans = -1
    while s<=e:
        m = (s+e)//2
        if N == m ** 3: #바로 세제곱이면
            ans = m
            break
        elif N< m**3: #다시 반씩...
            e = m-1
        else:
            s = m+1
    print(f'#{tc} {ans}')

#코드 2 - 얘는 이해됨 근데 위는 모르겟
t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    result = -1
    for i in range(1, n + 1):
        if i * i * i > n:  # 세제곱근보다 커지면 종료
            break

        if i * i * i == n:  # 같은 값이 있는지 확인
            result = i
            break

    print(f'#{tc} {result}')



#///////아래는 전부 런타임에러//////////
    # N = int(input())
    # X = -1
    # for i in range(2,N):
    #     if i*i*i==N:
    #         X = i
    #         break
    # print(f'#{tc} {X}')

    # N = int(input())
    # X = [(-1)]
    # for i in range(2,N):
    #     x = N/i/i
    #     if float.is_integer(x):
    #         if int(x) != 1:
    #             X.append(int(x))
    # print(f'#{tc} {X[-1]}')
