# pgms 코딩테스트 연습 - 연습문제 - 둘만의 암호

def rotate(aci):
    return (aci - 96) % 26 + 97
    # a-z 순환하는 함수

def solution(s, skip, index):
    answer = ''

    for c in s:
        aci = ord(c) # 이 함수를 몰라서
        for i in range(index):
            aci = rotate(aci)
            while chr(aci) in skip:
                aci = rotate(aci)
        ret = chr(aci)
        answer += chr(aci)
        # ord: 문자를 받고 유니코드 정수 반환, a가 97
        # chr: 정수를 받고 유니코드 문자 반환

    return answer