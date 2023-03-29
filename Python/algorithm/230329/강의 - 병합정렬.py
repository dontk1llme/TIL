# 병합정렬
def msort(m): #정렬
    if len(m)==1:
        return m

    middle = len(m)//2
    # left = []
    # right = []
    # for x in range(m[0:middle+1]):
    #     left.append(m[x])
    # for x in range(m[middle:]):
    #     right.append(m[x])
    left = m[:middle] #위 6줄을 이 두줄로 . . ..
    right = m[middle:] #=> 이렇게 하면 매번 만들어서 힘들어유 -> 밑에 개선된 방법으로 ㄱ

    left = msort(left)
    right = msort(right)
    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    msort(m)
#//////////////////////////////////////////////
# 개선된 방법~~
def msort(s,e):
    #sort
    if s==e:
        return
    m = (s+e)//2
    msort(s,m) #왼
    msort(m+1,e)  #오

    #merge
    k=0
    l,r = s,m+1 #왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l<=m or r<=e:
        if l<=m and r<=e:
            if lst[l]<=lst[r]:
                tmp[k] = lst[l]
                l+=1
            else:
                tmp[k]=lst[r]
                r+=1
        elif l<=m:
            while l<=m:
                tmp[k] = lst[l]
                l+=1
                k+=1
        elif r<=e:
            while r<=e:
                tmp[k]=lst[r]
                l+=1
                k+=1
    i=0 #여기까지 하면 결과가 tmp에 저장되어 잇음. 원본구간에 작업한거 넣어줘야함
    while i<k:
        lst[s+i]=tmp[i]
        i+=1
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tmp = [0]*N
    msort(0,N-1) #왼쪽, 오른쪽