# 코딩테스트 연습
# 완전탐색
# 최소직사각형

def solution(sizes):
    newarr = []
    for i in sizes:
        i = sorted(i)
        newarr.append(i)

    x, y = 0, 0
    for i in newarr:
        if i[0] > x: x = i[0]
        if i[1] > y: y = i[1]

    answer = x * y
    return answer