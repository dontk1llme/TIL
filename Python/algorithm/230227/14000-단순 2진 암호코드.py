#  [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 (제출용) D3
# 런타임 에러...... 근데 그럴만함 존나 돌아감

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(N)]

    #암호범위 추출
    #암호가 항상 1로 끝나서 뒤에서부터 찾음. #여기에서 for 두번 돌렷엇는데 한번만 하니까 런타임에러 안뜸
    k,l=0,0
    for i in range(N):
        for j in range(M-1,0,-1):
            if lst[i][j]=='1':
                k = i
                l = j
                break
    lst = lst[k][l-55:l+1]

    #2진수->10진수
    cnt=0
    numlst = []
    while lst:
        num = ''
        for i in range(7):
            num+=(str(lst.pop(0)))
        numlst.append(code[num])
        if len(numlst)==8:
            break

    #암호 확인
    c = (numlst[0]+numlst[2]+numlst[4]+numlst[6])*3 + numlst[1]+numlst[3]+numlst[5]+numlst[7]
    if c%10==0:
        ans = sum(numlst)
    else:
        ans = 0

    print(f'#{tc} {ans}')