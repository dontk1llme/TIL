# SWEA 1215. [S/W 문제해결 기본] 3일차 - 회문1 D3

# 1차원 배열에 str으로 입력받기
# 진행은 함수 만들어서 할게요...
# 가로는 그냥 진행하면 됨
# 세로는 새로운 str 배열 만들어서 진행해주면 되겟죠?

def pldr(lst, n):
    cnt = 0
    for k in lst:
        k = str(k) #얘도 str 안해주면 str취급을 안해주네......
        for l in range(len(k) - n + 1):
            str1 = k[l:l + n]
            # print(str1)
            if str1 == str1[::-1]:
                # print(f'회문:{str1}')
                cnt += 1
    return cnt

T = 10
for tc in range(1, T + 1):
    n = int(input())
    rowstrlst = list(input().split() for i in range(8))
    colstrlst = []
    for i in range(8):
        newstr=''
        for j in range(8):
            rowstr = str(*rowstrlst[j]) #str 없이 하니까 리스트 취급돼서 인덱스에러남
            newstr+=rowstr[i]
        colstrlst.append(newstr)

    row = pldr(rowstrlst, n)
    col = pldr(colstrlst, n)
    print(f'#{tc} {row+col}')

