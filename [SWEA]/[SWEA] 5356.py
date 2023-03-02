# 5356. 의석이의 세로로 말해요 (제출용) D3

T = int(input())
for tc in range(1, T+1):
    lst = [list(map(str, input())) for _ in range(5)]

    ans = ''
    #젤 긴 배열의 길이
    maxlen = 0
    for i in lst:
        if len(i)>maxlen:
            maxlen = len(i)

    for i in range(maxlen):
        for j in range(5):
            try: #인덱스 에러나면 걍 무시하세용
                ans += lst[j][i]
            except:
                continue
    print(f'#{tc} {ans}')
