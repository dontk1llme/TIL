# boj 2138 전구와 스위치
# https://velog.io/@dding_ji/baekjoon2138
# https://velog.io/@dding_ji/baekjoon2138
# 첫 스위치를 누르는 경우와 누르지 않는 경우로 분리!! <--- 이 생각 못 해서 헤맴...
# 마지막 스위치도 i+1 없는 거 주의


def change(now, to):
    l = now[:]
    press = 0
    for i in range(1, N):
        #이전 전구가 같은 상태면 pass
        if l[i-1] == to[i-1]:
            continue
        #다르면
        press+=1
        for j in range(i-1, i+2):
            if j<N:
                l[j]=1-l[j] #1이면 0되고 0이면 1됨
    return press if l==to else 1e9

N = int(input())
now = list(map(int,input()))
to = list(map(int,input()))

#첫 전구의 스위치를 누르지 않는 경우
ans = change(now, to)
#누르는 경우
now[0]=1-now[0]
now[1]=1-now[1]
ans = min(ans, change(now, to)+1)
print(ans if ans!=1e9 else -1)
