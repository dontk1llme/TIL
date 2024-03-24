# 코딩테스트 연습
# 2017 팁스타운
# 짝지어 제거하기

def solution(s):
    stack = []  # 스택을 초기화
    # 문자열 s의 각 문자에 대해 순회

    for i in s:
        # 스택이 비어있지 않고, 스택의 top에 있는 문자와 현재 문자가 같다면
        if stack and stack[-1] == i:
            stack.pop()  # 스택에서 pop을 합니다.
            continue  # 다음 문자로 넘어갑니다.
        stack.append(i)  # 그렇지 않다면 현재 문자를 스택에 push합니다.
    # 모든 문자를 순회한 후에 스택이 비어있다면 짝지어 제거하기가 성공적으로 수행된 것이므로 1을 반환
    # 그렇지 않다면 0을 반환
    print(stack)
    return int(not stack)

    # 시간초과 코드
#     answer = 0
#     tmp = s

#     while len(tmp)!=0:
#         for i in range(len(tmp)-1):
#             if tmp[i]==tmp[i+1]:
#                 tmp = tmp[:i]+tmp[i+2:]
#                 break;
#             elif i==len(tmp)-2:
#                 tmp = ''
#                 return 0
#                 break;
#         answer = 1

#     return answer