def f(i,k,s,key): #bit[i]를 결정하는 함수
    global cnt
    if i==k:
        if s==key:
            print(bit)
            cnt+=1
    else:
        bit[i]=0
        f(i+1, k, s, key) #A[i] 미포함
        bit[i]=1
        f(i+1, k, s+A[i], key) #포함

A = [i for i in range(1,11)]
N = 10
bit=[0]*N #어느 원소가 더해졌을 때 10이 되는지 확인 가능함
key = 10
cnt = 0
f(0,N,0,key)
print(cnt)