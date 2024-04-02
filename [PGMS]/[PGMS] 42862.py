# 코딩테스트 연습
# 탐욕법(Greedy)
# 체육복

def solution(n, lost, reserve):
    student = [0 for i in range(n + 1)]

    t1 = set(lost)
    t2 = set(reserve)

    lost = list(t1 - t2)
    reserve = list(t2 - t1)
    # 중복제거해줘야함 그래야 여벌 잇는 사람 도난당한 경우 체크 가능

    c = 0
    for i in lost:
        student[i] = 1
        c += 1
    print(c)

    for i in reserve:
        if i > 1 and student[i - 1] == 1:
            student[i - 1] = 0
            c -= 1
            continue
        if i < n and student[i + 1] == 1:
            student[i + 1] = 0
            c -= 1

    return n - c