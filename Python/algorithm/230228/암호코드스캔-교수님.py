dct = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
dct2 = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def solve():
    ans = set()
    for st in sset:
        # [1] 16진수 문자열 => 2진수 문자열로
        bst = ''
        for ch in st:
            bst += dct[ch]
        # print(bst)

        # [2] 연속한 0/1의 개수 저장
        cnts = []
        old = 0
        for i in range(len(bst)):
            if bst[old] != bst[i]:
                cnts.append(i - old)
                old = i
        # print(cnts)

        # [3] 단위두께로 나누어서 암호로 변환: 224 => 112
        pwd = []
        for i in range(1, len(cnts), 4):
            mn = min(cnts[i:i + 3])
            key = str(cnts[i] // mn) + str(cnts[i + 1] // mn) + str(cnts[i + 2] // mn)
            pwd.append(dct2[key])
        # print(pwd)

        # [4] pwd의 8자리씩 코드를 중복제거
        for i in range(0, len(pwd), 8):
            ans.add(tuple(pwd[i:i + 8]))

    # [5] ans에서 암호코드를 하나씩 꺼내서 검증 후 정상이면 누적
    sm = 0
    for lst in ans:
        if (sum(lst[0:8:2]) * 3 + sum(lst[1:8:2])) % 10 == 0:  # 정상인 경우 누적
            sm += sum(lst)
    return sm


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 입력문자열 중복제거
    sset = set()
    for _ in range(N):  # N줄의 문자열을 입력
        st = input()
        if st.count('0') != len(st):
            sset.add(st)

    ans = solve()
    print(f'#{tc} {ans}')