# swea 4836 색칠하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    

    newarr = [[0]*100 for _ in range(100)]
    for i in arr:
        for j in range(i[0],i[2]+1):
            for k in range(i[1],i[3]+1):
                newarr[j][k]+=i[4] #색깔을 더함. 같은 색끼리는 안 겹친다고 했으니까
    
    cnt = 0
    for l in range(len(newarr)):
        for m in range(len(newarr)):
            if newarr[l][m]>=3:
                cnt+=1
    
    print(f'#{tc} {cnt}')


