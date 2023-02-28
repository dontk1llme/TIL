# 1
dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
       '0110111': 8, '0001011': 9}


def solve(arr):
    for st in arr:
        if '1' in st:  # '1'이 있는 경우 처리
            # [1] 끝부터 처음 1을 만나는 지점 찾기: e
            for e in range(len(st) - 1, -1, -1):
                if st[e] == '1':
                    break

            # [2] 7자리씩 숫자로 변환
            pwd = []
            for i in range(e - 55, e + 1, 7):
                pwd.append(dct[st[i:i + 7]])
            # print(pwd)

            # [3] 검증(짝수위치*3 + 홀수위치 가 10의 배수)
            if (sum(pwd[0:8:2]) * 3 + sum(pwd[1:8:2])) % 10 == 0:
                return sum(pwd[0:8:2]) + sum(pwd[1:8:2])
            return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve(arr)
    print(f'#{tc} {ans}')


# 2 (좀 더 일반화)
dct = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def solve(arr):
    for st in arr:
        if '1' in st:  # '1'이 있는 경우 처리
            cnts = []
            old = 0
            # [1] 0과 1의 연속한 개수 저장
            for i in range(len(st)):
                if st[old] != st[i]:
                    cnts.append(i - old)
                    old = i
            # print(cnts)

            # [2] 개수를 디코딩해서 암호로 변환/저장
            pwd = []
            for i in range(1, len(cnts), 4):
                pwd.append(dct["".join(map(str, cnts[i:i + 3]))])
            # print(pwd)

            # [3] 검증(짝수위치*3 + 홀수위치 가 10의 배수)
            if (sum(pwd[0:8:2]) * 3 + sum(pwd[1:8:2])) % 10 == 0:
                return sum(pwd[0:8:2]) + sum(pwd[1:8:2])
            return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve(arr)
    print(f'#{tc} {ans}')