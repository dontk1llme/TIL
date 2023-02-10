N,M = map(int, input().split())
cnt = 0
for i in range(N, M+1):
    sqrt = N**(1/2) #제곱근
    if sqrt%1==0:
        print(sqrt)
        cnt+=1
print(cnt)