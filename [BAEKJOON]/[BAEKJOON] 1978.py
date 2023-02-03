#[BAEKJOON] 1978 소수찾기

N = int(input())
ls = list(map(int, input().split()))
cntcnt=0

for n in range(N):
    cnt =0
    if ls[n] == 1: continue
    for j in range(2,ls[n]+1): #+1을 해줘야 본인까지 포함이라 소수면 본인만 잇기땜에 카운트
        if ls[n]%j==0: #나눠떨어지는지. 1과 본인 아닐 때 떨어지면 소수 아님
            cnt+=1
    if cnt==1:
        cntcnt+=1
print(cntcnt)
