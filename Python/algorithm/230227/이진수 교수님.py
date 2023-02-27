T = int(input())
for tc in range(1, T + 1):
    _, st = input().split()
    alst = []
    for ch in st:
        # [1] 16진수 => 10진수로 변환
        if ch.isdigit():
            n = ord(ch) - ord('0')
        else:
            n = ord(ch) - ord('A') + 10

        # [2] 10진수를 2진수로 변환
        for pos in (3, 2, 1, 0):  # 16진수는 4비트로 구성
            alst.append((n >> pos) & 1)
    print(f'#{tc} {"".join(map(str, alst))}')