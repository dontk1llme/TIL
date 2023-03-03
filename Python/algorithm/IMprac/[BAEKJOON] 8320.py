# [BAEKJOON] 8320 직사각형을 만드는 방법
# 오... 진짜 모르겟는데?
# 규칙 찾기 중요!
# https://pacific-ocean.tistory.com/178

N = int(input())
cnt=N
for i in range(2, int(N**0.5)+1):
    for j in range(i,N):
        if i*j<=N:
            cnt+=1
        else:
            break
print(cnt)