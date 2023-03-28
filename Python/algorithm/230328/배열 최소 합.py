#  [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 (제출용) D2
#  딱봐도 백트래킹
#  https://glory-summer.tistory.com/82

def section_sum(idx, total): #idx: 현재 행, 현재까지합:total, DFS임
    global ans

    if idx==N: #모든 행을 돌았을 때
        if total<ans:
            ans=total
            return
    if total>ans: #가지치기
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            section_sum(idx+1, total+lst[idx][i])
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 90 #최대 90. . .
    visited = [] #x,y를 넣는 게 아님. 그냥 지나온 열들만 넣어주면 되는거임
    section_sum(0,0)
    print(f'#{tc} {ans}')