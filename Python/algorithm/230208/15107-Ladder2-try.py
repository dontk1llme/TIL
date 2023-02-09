#Ladder2

T = 1
for test_case in range(1, T + 1):
    _ = input()
    N = 100
    # 좌, 우 양쪽을 0으로 padding해서 입력
    orarr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    # 반복해야 하는데 얕은복사 피해주기 위해서 이렇게 새로 만듦...
    # 미친거니? 함수쓰면되는데 https://crackerjacks.tistory.com/14
    def againarr():
        lll = [[0] * N for _ in range(N)]
        for i in range(len(orarr)):
            for k in range(len(orarr)):
                lll[i][k] = orarr[i][k]
        return lll

    ci = 0 #맨윗줄에서 찾을거니까...
    cnt = 1000 #최단시간
    ans = 0 #출력할 답

    # [1] 시작위치(1) 찾기
    arr = againarr()
    yarr=[] #시작 위치 인덱스 모음
    for j in range(N):
        if arr[ci][j] == 1:
            yarr.append(j)

    # [2] N-1행 시작위치에서 아래쪽으로 사다리이동
    for y in yarr:
        nowcnt=0
        while ci < 100:
            arr[ci][y] = 0  # 재방문 방지
            if arr[ci][y - 1]:  # 왼쪽!
                y -= 1  # 이동
                nowcnt+=1
            elif arr[ci][y + 1]:  # 오른쪽!
                y += 1  # 이동
                nowcnt += 1
            else:
                ci += 1  # 아래쪽이동
                nowcnt += 1
        # ci와 arr 다시 원상태로
        ci=0
        arr = againarr()

        # 현재시간(nowcnt)이 이전것(cnt)보다 작으면 cnt와 ans 변경
        if nowcnt<cnt:
            cnt = nowcnt
            ans = y
        print(f'답: {ans}, 지금위치: {y}, 횟수:{cnt}')

    print(f'#{test_case} {ans}')