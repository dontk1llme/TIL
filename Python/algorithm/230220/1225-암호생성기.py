#미리 풀어두었던 암호생성기... ~

T = 10
for _ in range(T):
    tc = int(input())
    numlst = list(map(int, input().split()))

    minus=1
    while True:
        if minus>5: #조건도 다 고려한 뒤에 일처리하면 쉽네요
            minus=1
        tmp = numlst.pop(0)-minus
        if tmp<=0:
            numlst.append(0)
            break
        numlst.append(tmp)
        minus+=1


    print(f'#{tc}', end=' ')
    print(*numlst)