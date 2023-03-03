# [BAEKJOON] 8958 OX퀴즈

T = int(input())
for tc in range(T):
    ox = input()
    now = 0
    ans = 0
    for i in ox:
        if i=='O':
            now+=1
            ans+=now
        else: now = 0
    print(ans)
