# 10804. 문자열의 거울상 D3

# 딕셔너리로 풀었어야된다네요 교수님이..........
T = int(input())
for tc in range(1, T+1):
    strs = input()
    ans = ''
    strs = strs[::-1]
    #거울을 옆에서 비춘다고 생각해야...
    for i in range(len(strs)):
        if strs[i] == 'b':
            ans+='d'
        elif strs[i] == 'd':
            ans+='b'
        elif strs[i] == 'p':
            ans+='q'
        elif strs[i]=='q':
            ans+='p'


    print(f'#{tc} {ans}')

    # 거울을 아래서 비추면...
    # for i in range(len(strs)):
    #     if strs[i] == 'b':
    #         ans+='p'
    #     elif strs[i] == 'd':
    #         ans+='q'
    #     elif strs[i] == 'p':
    #         ans+='b'
    #     elif strs[i]=='q':
    #         ans+='d'

    #교수님 풀이
    #1. 파이써닉하지 못한 (C나 자바)
    # tbl = [0] * 128
    # tbl[ord('b')] = 'd'
    # tbl[ord('d')] = 'b'
    # tbl[ord('p')] = 'q'
    # tbl[ord('q')] = 'p'
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     st = input()[::-1]
    #     alst = []
    #     for ch in st:
    #         alst.append(tbl[ord(ch)])
    #     print(f'#{test_case} {"".join(map(str, alst))}')

    #2. 파이써닉: 딕셔너리 (빠름)
    # dct = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'}
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     st = input()[::-1]
    #     alst = []
    #     for ch in st:
    #         # alst.append(tbl[ord(ch)])
    #         alst.append(dct[ch])
    #     print(f'#{test_case} {"".join(map(str, alst))}')