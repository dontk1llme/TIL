# 코딩테스트 연습
# Summer/Winter Coding(~2018)
# 영어 끝말잇기

def solution(n, words):

 words_set = set() # 사용된 단어를 저장하기 위한 set() 생성 / 중복 방지용
 words_set.add(words[0]) # 첫 번째 단어를 세트에 추가

# 두 번째 단어부터 마지막 단어까지 순회
 for i in range(1, len(words)):

    # 만약 현재 단어가 이미 사용된 단어이거나
    # 이전 단어의 마지막 글자와 현재 단어의 첫 글자가 다르다면
    if (words[i] in words_set) or (words[i-1][-1] != words[i][0]):

    # 탈락자의 번호와 차례를 반환
    # 번호는 인덱스를 사람 수로 나눈 나머지에 1을 더한 값
    # 차례는 인덱스를 사람 수로 나눈 몫에 1을 더한 값
        return [(i%n)+1, (i//n)+1]
    # 현재 단어를 사용된 단어의 set()에 추가
    words_set.add(words[i])
    # 모든 단어가 규칙에 맞게 사용되었다면 [0, 0]을 반환
    return [0, 0]