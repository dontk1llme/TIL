# 1989. 초심자의 회문 검사 D2

T = int(input())
for tc in range(1,T+1):
    strr = input()
    ans=0
    if strr==strr[::-1]:
        ans=1
    print(f'#{tc} {ans}')

#왜 위는 오답이고 아래는 정답임? 걍 같은거 아님?
#아니네 본문 프린트 안뺌 ㅋㅋ

# def palindrome(word):
#     if word == word[::-1]:
#         return 1
#
#     else:
#         return 0
# test_case = int(input())
#
# for i in range(test_case):
#     word = input()
#
#     print(f'#{i + 1}', end=' ')
#
#     print(palindrome(word))