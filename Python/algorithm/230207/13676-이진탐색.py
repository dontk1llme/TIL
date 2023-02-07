T = int(input())
for tc in range(1, T+1):
    P,A,B = map(int, input().split()) #전체, A거, B거
    arr=[*range(P)] #얘도 1,P 말고 그냥 P

    def binarySearch(arr,D):
        # 10개중 8개 맞음 - end = mid-1,start = mid+1로 했더니 잘못된 경우 발생
        # 문제대로 하기...
        # start=0
        # end=P-1 #인덱스는 N-1까지
        start = 1
        end = P
        cnt=0
        while start<=end:
            cnt+=1
            mid = int((start+end)/2)
            if arr[mid]==D: #검색 성공
                break
            elif arr[mid]>D:
                # end=mid-1 #구간의 끝을 줄임
                end = mid
            else:
                # start=mid+1 #구간의 시작을 줄임
                start = mid
            #mid+-1 안 하는 이유: 예제에서 그렇게 돼 잇어서... 201이 아니라 200으로 햇음...
        return cnt  # 검색 횟수 리턴
    #A의 이진 탐색
    a = binarySearch(arr,A)

    #B의 이진 탐색
    b = binarySearch(arr,B)


    #검색 횟수가 적은 게 답임
    if a>b: ans='B'
    elif a<b: ans='A'
    else: ans=0

    print(f'#{tc} {ans}')


    # https://github.com/BY1994/hphk_001/blob/master/Algorithms/190124_03_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89.py

    # def binarySearch(n, key):
    #     l = 1
    #     r = n
    #     cnt = 0
    #     while 1 :
    #         mid = int((l + r) / 2)
    #         cnt += 1
    #         if mid == key:
    #             break
    #         if mid < key:
    #             l = mid
    #         else :
    #             r = mid
    #     return cnt
    #
    # TC = int(input())
    # for tc in range(1, TC+1):
    #     pages, key1, key2 = map(int, input().split())
    #     cnta = binarySearch(pages, key1)
    #     cntb = binarySearch(pages, key2)
    #
    #     result = '0'
    #     if cnta < cntb:
    #         result = 'A'
    #     elif cnta > cntb:
    #         result = 'B'
    #
    #     print('#%d %c'%(tc, result))


