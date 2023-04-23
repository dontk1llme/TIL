# 1687. 데일리실습 4-1. 반복문을 활용한 비밀번호 유효성 

correct = '0486'
trylist = ['']*2
try:
    for i in range(0,3):
        pw = input('비밀번호를 입력하세요.: ')
        if pw == correct:
            print("맞는 비밀번호입니다.")
            break
        else:
            trylist[i]=pw
except: print("비밀번호를 3번 이상 틀렸습니다.")