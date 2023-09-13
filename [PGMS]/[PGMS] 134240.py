# PGMS 134240 푸드 파이트 대회
def solution(food):
    result = ''
    for i in range(1, len(food)):
        result += (str(i)*(food[i]//2))
    return result + '0' + result[::-1]

    #간결화 참고 https://velog.io/@nellroll/%ED%91%B8%EB%93%9C-%ED%8C%8C%EC%9D%B4%ED%8A%B8-%EB%8C%80%ED%9A%8C