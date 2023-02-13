# 두더지 잡기 게임

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 두더지 머리 내미는 횟수
    r, c = map(int, input().split())  # 시작 망치 위치 (1초에 한 칸 이동 가능, 가로부터)
    point = 0  # 획득점수
    for n in range(N):
        a, b, k = map(int, input().split())  # a,b: 두더지 좌표, k: 내밀고 있는 시간

        # 득점여부
        movetime = abs(r - a) + abs(c - b)
        if movetime <= k: point += 1

        # 망치 좌표 이동하기
        time = 0
        while time < k:
            for i in range(abs(c - b)):  # 가로부터
                if c > b:
                    c -= 1
                    time += 1
                else:
                    c += 1
                    time += 1
                if (r == a and c == b) or time == k: break  # 좌표가 같아지거나 시간이 되면 멈춤
            if (r == a and c == b) or time == k: break
            for j in range(abs(r - a)):  # 세로
                if r > a:
                    r -= 1
                    time += 1
                else:
                    r += 1
                    time += 1
                if (r == a and c == b) or time == k: break  # 좌표가 같아지거나 시간이 되면 멈춤
            if (r == a and c == b) or time == k: break


    print(f'#{tc} {point}')
