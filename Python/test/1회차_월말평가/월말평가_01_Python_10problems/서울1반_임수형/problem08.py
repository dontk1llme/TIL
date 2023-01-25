# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    word에 있는 글자 하나씩 변환해서 ans string에 합쳐주자.
    변환 전 대/소문자 비교를 하고, 아스키 코드로 변환 후 n을 더해주자.
    더한 값이 122를 넘어설 경우 a부터 다시 시작이기 때문에 58을 빼주자.
    다시 문자로 변환하고, 이전 대/소문자 비교한 것을 반영해서 합쳐주자.
    '''

    ans = ''
    for i in word:
        is_upper = i.isupper()
        g = ord(i) + n
        if g > 122:
            g = g - 58

        if is_upper:
            ans = ans + chr(g).upper()
        else:
            ans = ans + chr(g).lower()

    return ans 



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
