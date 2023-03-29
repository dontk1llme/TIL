#  [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 (제출용) D3
# 문제 이해가 안되네
# y=0에서 출발해서 임의의 x값들을 중복되지 않게 모두 바꾼 다음 마지막 사무실로 돌아오는것(x==0)
# y값 다음에는 x값이 되는 이어지는 원리라는데요
# https://independenceday.tistory.com/entry/SWEA-5189-%EC%A0%84%EC%9E%90%EC%B9%B4%ED%8A%B8-python

T = int(input())

def battery(cnt, y, total):
    global ans

    if total>ans: #가지치기.
        return

    if cnt==N: #마지막은 무조건 사무실 돌아와야 함
        total += lst[y][0]
        if total<ans:
            ans=total
            return

    for i in range(1,N): #마지막 경우 빼고 돌려주기
        if not lst[y][i]: #n,n이면 0이니까 넘기기
            continue
        if not visited[i]:
            visited[i]=1
            battery(cnt+1, i, total+lst[y][i])
            visited[i]=0

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = N * 100 #최대값
    battery(1,0,0)
    print(f'#{tc} {ans}')