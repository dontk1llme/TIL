# [BAEKJOON] 2999 비밀 이메일
# 얘들아 헤어져라

s = input()

#행렬
N = len(s)
yaklst =[]
for i in range(1,N+1): #가장 큰 약수
    if N%i==0:
        if i not in yaklst and N//i not in yaklst:
            yaklst.append(i)
        else: break
C = max(yaklst)
R = N//C
lst = [[0] * C for _ in range(R)]

#넣기
idx=0
for i in range(R):
    for j in range(C):
        lst[i][j] = s[idx]
        idx+=1

#옮기기
for i in range(C):
    for j in range(R):
        print(lst[j][i],end='')


