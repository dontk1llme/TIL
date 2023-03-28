#  [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 (제출용) D2
# 짧은 작업 우선 X. 먼저 시작 우선 X. 빨리 종료 우선!
# 교수님 코드

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간 기준 오름차순 정렬
    lst.sort(key=lambda x: x[1])

    # 직전 종료 시간보다 크거나 같은 경우 할당
    end = ans = 0
    for s,e in lst:
        if end<=s: #할당 가능
            ans+=1
            end=e

    print(f'#{tc} {ans}')