# [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 (제출용) D2
# https://velog.io/@wltn39/SWEA-4881-%EB%B0%B0%EC%97%B4%EC%B5%9C%EC%86%8C%ED%95%A9
# 백트래킹 써야 함... 아래 풀이가 정석인듯
# 전형적인!

def minSum(row, N, now, visited):
    global ans
    if row == N:  # i가 배열의 수와 일치하면
        if now < ans:
            ans = now
    elif now > ans: #얘 없으면 시간초과
        return
    else:
        for col in range(N):
            if not visited[col]:  # 방문 전 칼럼
                visited[col] = 1  # 방문
                # 다음 row로 넘어가고,now에 값을 더해주고, visited 갱신
                minSum(row + 1, N, now + lst[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화 (재검색 가능하도록) !!!!!걍 이 식은 외워


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # NxN 배열에 숫자가 들어있음
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 100
    visited = [0] * N  # 방문했는지!
    minSum(0, N, 0, visited)
    print(f'#{tc} {ans}')

# 3
# 2 1 2
# 5 8 5
# 7 2 2
# 2 -> (5) 8 5 ->
# 1 -> (5) 8 5 ->