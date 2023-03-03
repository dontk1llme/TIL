# [BAEKJOON] 2810 컵홀더

N = int(input())
lst = input()

i = 0
cnt = 1 #왼쪽 끝 좌석
while i<N:
    if lst[i]=='S':
        cnt+=1
        i+=1
    elif lst[i]=='L':
        cnt+=1
        i+=2

ans = cnt
if ans > N:
    ans = N
print(ans)