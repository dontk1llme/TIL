#swea 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3

T = int(input())
for _ in range(T):
    strr = input()
    i = len(strr)
    print('.' + '.#..' * i)
    print('.' + '#.' * i * 2)
    print('#', end='')
    for j in range(1,i+1):
        print(f'.{strr[j-1]}.#', end='')
    print()
    print('.' + '#.' * i * 2)
    print('.' + '.#..' * i)
#ㅋㅋ 이렇게해도됨? 아닌거같은데
#https://deok2kim.tistory.com/262
#     a = '..#.'
#     b = '.#.#'
#     ab_last = '.'
#     c1 = '#.'
#     c2 = '.'
#     c_last = '#'
#
#     N = len(word)
#     answer = ['']*5
#     answer[0] += a*N + ab_last
#     answer[1] += b*N + ab_last
#     for w in word:
#         answer[2] += c1 + w + c2
#     answer[2] += c_last
#     answer[3] += b*N + ab_last
#     answer[4] += a*N + ab_last
#
#     for rw in answer:
#         print(rw)