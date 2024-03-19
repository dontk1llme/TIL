# 코딩테스트 연습
# 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    lst2 = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'  # 2단계
    tmp = ''
    for c in answer:
        if c in lst2: tmp += c
        # 혹은 if c.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.' 사용
    answer = tmp
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    while answer.startswith('.') or answer.endswith('.'):
        if answer.startswith('.'): answer = answer[1:]
        if answer.endswith('.'): answer = answer[:-1]
    # 5단계
    if answer == '': answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer = answer + answer[-1]

    return answer