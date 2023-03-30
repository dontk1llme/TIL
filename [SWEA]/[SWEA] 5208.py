#  5208 [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 (제출용) D3
# https://velog.io/@daon9apples/SWEA-D3-5208.-%ED%8C%8C%EC%9D%B4%EC%8D%AC-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EA%B5%AC%ED%98%84-5%EC%9D%BC%EC%B0%A8-%EC%A0%84%EA%B8%B0%EB%B2%84%EC%8A%A42-python

def dfs(idx):
    global ans, charge

    if ans<=charge: #가지치기
        return

    if idx>=len(lst): #종료->목적지보다 더 가면 통과니까
        if ans>=charge:
            ans = charge
        return

    for i in range( idx+lst[idx], idx, -1): #멀리서부터 . . . 갈 수 있는 정류장 다 따지기
        charge+=1
        dfs(i)
        charge-=1


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))  # lst[0]:정류장 수, lst[1:] 배터리별 용량

    ans = lst[0] * lst[0]  # 최소 교환횟수 -> 우선 최대값으로
    charge = 0 #현황
    dfs(1)

    print(f'#{tc} {ans-1}') #-1: 시작하는 곳은 안치니까. . .

#////////////////////////////////////
# 개짧은코드
def dfs(n, cnt):
    global ans
    if cnt >= ans:
        return
    if n >= N - 1:
        ans = min(ans, cnt)
        return

    for i in range(battery[n]):
        dfs(n + i + 1, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    battery = lst[1:]
    ans = N - 1
    dfs(0, -1)
    print(f'#{tc} {ans}')