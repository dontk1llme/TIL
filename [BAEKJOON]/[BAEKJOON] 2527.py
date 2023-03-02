# BOJ 2527 직사각형

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    if p1<x2 or p2<x1 or y1>q2 or q1<y2: #공통부분 없음
        print('d')
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1: #점
            print('c')
        else: #선분
            print('b')
    elif q1==y2 or q2==y1: #선분
        print('b')
    else:
        print('a')