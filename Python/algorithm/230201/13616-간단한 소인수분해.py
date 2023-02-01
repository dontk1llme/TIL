# 1945
T = int(input())

for k in range(1, T+1):
    num = int(input())
    nlist=[2,3,5,7,11] # 얘 만들어서 하는게 훨씬 효율적이네
    count=[0]*5

    for i in range(len(nlist)):
        while True:
            if num % nlist[i] == 0:
                num = num//nlist[i]
                count[i]+=1
            else: break

    print(f'#{k}', end=' ')
    for j in count:
        print(j, end=' ')
    print('')