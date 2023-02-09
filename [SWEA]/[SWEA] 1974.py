#1974. 스도쿠 검증 D2
# ㅇ얘네 이거 이렇게 하나씩 하면 안되는거같은데???? 세 경우 다 한번에 봐야되는거 같은데
# 아니네 그냥 이렇게해도 되네 ㅎ.ㅎ
# 중복없으면 괜찮게하면 되자나요
# list comprehension과 zip 사용법을 알면 편하겟네요

T = int(input())
for tc in range(1, T+1):
    #2차원 배열 입력받기
    sdk = [list(map(int, input().split())) for _ in range(9)]
    ans=1
    #가로
    row = sdk
    col = [[sdk[i][j] for i in range(9)] for j in range(9)]
    sqr = [[sdk[i%3*3+j//3][i//3*3+j%3] for j in range(9)]for i in range(9)] #3*3 사각형! 식 주의
    for r,c,s in zip(row,col,sqr):
        if len(set(r)) == len(set(c)) == len(set(s)) == 9:
            continue
        else:
            ans = 0
            break
    print(f'#{tc} {ans}')

    #
    #
    # #가로
    # for i in range(len(sdk)):
    #     ls1 = sorted(sdk[i])
    #     if list(jb)==ls1: ans=1
    #
    #
    # #세로
    # collst=[[0]*9 for _ in range(9)]
    # for i in range(len(sdk)):
    #     for j in range(len(sdk)):
    #         collst[i][j]=sdk[j][i]
    #     print(collst[i])
    #     ls2 = sorted(sdk[i])
    #     if list(jb)==ls2: ans=1
    #
    #
    # #칸
    #
    #
    # print(f'#{tc} {ans}')