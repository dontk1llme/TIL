T = int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split()) #N개의 글자를 가짐, 길이가 M인 회문 찾기
    strs = [input() for _ in range(N)] #1차원 배열
    result = [] #답 넣을 곳

    #가로 확인
    for i in range(N):
        for j in range(N-M+1):
            if strs[i][j:j+M] == strs[i][j:j+M][::-1]: #잘라서 안 해도 되네.. 범위만 보면 되네
                result.append(strs[i][j:j+M])

    #세로 확인
    newstr = [] #세로 문자열
    for k in range(len(strs)):
        n = ''
        for l in range(len(strs)):
            n += strs[l][k]
        newstr.append(n)
    for i in range(N):
        for j in range(N-M+1):
            if newstr[i][j:j+M] == newstr[i][j:j+M][::-1]:
                result.append(newstr[i][j:j+M])


    print(f'#{tc} {result[0]}')