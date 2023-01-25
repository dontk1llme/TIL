# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_good_rate(movie):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    if 조건문을 사용하여 8을 기준으로 is_bool 변수에 bool값을 지정해주자.
    '''
    rating = movie["user_rating"]

    if rating >= 8:
        is_bool = True
    else:
        is_bool = False
    return is_bool

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(is_good_rate(movie))  # True