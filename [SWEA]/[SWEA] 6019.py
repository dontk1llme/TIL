# [SWEA] 6019 기차 사이의 파리 D3

T = int(input())
for tc in range(1,T+1):
    #D: 기차 전면부 사이의 거리, A: 기차A속력, B:기차B속력, F:파리속력
    D,A,B,F = map(float, input().split()) #답에 200.000 이렇게 돼잇어서 int하면틀리고 float하면맞음

    #sec=0
    ans=0
    now=0
    while(D > 0):
        #sec+=1 #1초 지남
        D = D-(A+B)
        ans += F
        now += F
        if now == D:
            now = 0
    #print(sec) #몇초뒤에 파리 뒤지는지
    #print(ans) #파리가 뒤지기 전까지 날아다닌 거리
    print(f'#{tc} {ans}')



# 이게 답이래 미친거아니냐?
# T = int(input())
# for t in range(1,T+1):
#     D, A, B, F = map(int, input().split())
#
#     print('#{} {}'.format(t,(D/(A+B)) * F)) #거속시 공식이래.................열받아...