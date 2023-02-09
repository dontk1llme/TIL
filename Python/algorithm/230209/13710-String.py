T = 10
for tc in range(1,T+1):
    n=int(input())
    f = input()
    a = input()

    cnt = 0
    for i in range(len(a)-len(f)+1): #인덱스에러 주의
        k = i
        ff = ''
        for j in range(len(f)):
            ff+=a[k]
            k+=1
        if ff==f:
            cnt+=1


    print(f'#{n} {cnt}')