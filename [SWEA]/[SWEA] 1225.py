# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3

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


# 아미친. 큐로 풀어라
# minus=1
# while minus<6:
#     numlst[0] -= minus  # 감소 후
#     minus += 1
#     tmp = numlst[0]
#     for i in range(len(numlst) - 1):  # 뒤로 이동
#         numlst[i] = numlst[i + 1]
#     numlst[-1] = tmp
#     if numlst[-1] <= 0:
#         numlst[-1] = 0
#         break

#
# for minus in range(1, 6):
#     numlst[0]-=minus #감소 후
#     tmp = numlst[0]
#     for i in range(len(numlst)-1): #뒤로 이동
#         numlst[i] = numlst[i+1]
#     numlst[-1] = tmp
# if numlst[-1]<=0:
#     numlst[-1]=0
#     break






