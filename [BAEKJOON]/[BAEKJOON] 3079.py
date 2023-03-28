# boj 3079 입국심사
# 그리디나 브루트포스로 문제를 풀면 M의 최대 크기가 10억이라 시간초과!
# https://dreamtreeits.tistory.com/199
# https://www.acmicpc.net/board/view/67774

N,M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

l, r = min(lst), max(lst) * M #l:한 명이 받는 최소 시간, r: m명이 받는 최대 시간
ans = r

while l<=r:
    total = 0
    mid = (l+r)//2

    for i in range(N):
        total += mid//lst[i] #n초동안 최대로 심사 가능한 사람의 합을 구하는 과정

    if total >= M: #모든 인원이 심사대에서 심사를 받았다면
        r = mid-1 #더 작은 최소 시간이 있는지 확인
        ans =min(mid, ans)
    else:
        l = mid+1

print(ans)