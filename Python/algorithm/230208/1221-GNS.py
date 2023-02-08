# 1221. [S/W 문제해결 기본] 5일차 - GNS D3

T = int(input())
for tc in range(1, T+1):
    N, L = map(str, input().split())
    strls = list(map(str, input().split()))
    count = ['ZRO', 'ONE', 'TWO', 'THR','FOR','FIV','SIX','SVN','EGT','NIN']
    numls = []
    for k in count:
        for i in range(len(strls)):
            if strls[i] == k:
                numls.append(strls[i])

    print(N)
    print(*numls)

