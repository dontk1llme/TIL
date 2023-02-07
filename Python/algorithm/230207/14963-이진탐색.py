T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))

    def binarySearch(arr,N,D):
        start=0
        end=N-1 #인덱스는 N-1까지
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==D: #검색 성공
                return mid+1
            elif arr[mid]>D:
                end=mid-1 #구간의 끝을 줄임
            else:
                start=mid+1 #구간의 시작을 줄임
        return 0 #검색 실패

    print(f'#{tc} {binarySearch(arr,N,D)}')
