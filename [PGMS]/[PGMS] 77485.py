# pgms 77485 2021 dev-match 행렬 테두리 회전하기
# 에엥 타임에러............................... 머지?...........
# https://school.programmers.co.kr/questions/29760 내일 오면 이거 읽어보기
# 아니 행렬 다 맞게 줬고 만들어지는것도 잘 만들어지는데

rows = 100
columns = 97
queries = 	[[1,1,98,2]]
# queries = 	[[1,1,100,97]]
# 얘가 1,1,98,97 되는순간 망함..
# 1,1,98,2여도 망함
# 근데 또 10 9 이런식은 됨... 왼쪽이 크다고 항상 망하는거는 아님 걍 98 이상되면 망ㅎㅏㅁ
# res = [1]

d = [(0,1), (1,0), (0,-1), (-1,0)]#우 하 좌 상

def solution(rows, columns, queries):
    cnt = 0
    # map = [[0] * rows for _ in range(columns)]  # map 만들기 . ..
    # cnt = 1
    # for i in range(columns):
    #     for j in range(rows):
    #         map[i][j] = cnt
    #         cnt += 1
    map = [[columns * i + j for j in range(1, columns + 1)] for i in range(rows)]
    answer = []
    for i in queries:
        x1,y1,x2,y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1 #인덱스화해서 나누기. 고정놈들
        x,y = x1,y1 #움직일놈들
        tmp = map[x][y]
        tmpans = []
        didx= 0

        while True:
            cnt+=1
            nx, ny = x+d[didx][0], y+d[didx][1]
            if 0<=nx<rows and 0<=ny<columns: #미친놈아 똑바로안볼래?? x가 row라잖아. . . 그리고 이 코드 없어도 돌아감
                tmpans.append(tmp)
                tmp, map[nx][ny] = map[nx][ny], tmp #바꾸고
                x, y = nx, ny #인덱스도 옮겨주고

                if didx==0 and y==y2: didx+=1
                elif didx==1 and x==x2: didx+=1
                elif didx==2 and y==y1: didx+=1
                elif didx==3 and x==x1: break
        #     print(x, y, nx, ny)
        #     print(cnt)
        # print(tmpans)
        # print(*map)
        answer.append(min(tmpans))

    return answer

print(solution(rows, columns, queries))