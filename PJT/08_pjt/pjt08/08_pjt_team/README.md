# PJT08 - 서울 1반 임혜진, 이예슬

### A. 유저 팔로우 기능

AJAX 통신을 이용, 비동기적으로 팔로우 기능 구현
- 유저 팔로우 기능
    - 팔로우 버튼을 클릭하는 경우, 페이지가 새로고침 되는 것이 아니라 AJAX 통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성
    - `views.py 의 follow 함수`
        - 회원 가입자만 이용이 가능하게 하고 팔로우, 팔로잉 여부와 그 누적 수를 카운팅하여 JsonResponse로 보냄
    - `profile.html`
        - form이 실행되면 scripts로 결과 를 가져와 비동기식으로 팔로우 기능만 동작


### B. 리뷰 좋아요 기능

AJAX 통신을 이용, 비동기적으로 좋아요 기능 구현
- 리뷰 좋아요 기능
    - 좋아요 버튼을 클릭하는 경우, AJAX통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성
    - `views.py의 like 함수`
        - 회원 가입자만 이용이 가능하게 하고 좋아요 클릭 여부에 따라 좋아요 버튼의 상태를 다르게 구현해 줬으며, 해당 카운팅을 JsonResponse로 보냄
    - `index.html`
        - 좋아요 버튼이 클릭되면 ‘좋아요 취소’ 가 나오면서 카운팅을 갱신
        - 좋아요 취소 버튼이 클릭되면 ‘좋아요’가 나오면서 카운팅을 갱신

### C. Movies 앱 기능

1. 전체 영화 목록 조회 (index)

전체 영화 데이터의 쿼리셋을 불러와서 출력함

2. 단일 영화 상세 조회 (detail)

해당 영화 데이터 쿼리를 불러와서 출력함

3. 영화 추천 기능 (recommended)

사용자가 추천 받고 싶은 영화 장르를 선택하면 그 장르에 해당하는 영화를 출력함
- Movies 앱 기능
    1. 전체 영화 목록 조회 (`Index.html`)
        - Movie 모델 쿼리 셋에서 모든 데이터를 받아 출력
        - 부트스트랩 사용
    2. 단일 영화 상세 조회 (`detail.html`)
        - index.html의 전체 영화 목록에서 영화 포스터를 클릭하면 영화에 대한 상세 정보가 나오도록 구현
        - genre가 Genre form에 들어있기 때문에 해당 부분을 역참조 하여 해결
    3. 영화 추천 기능 (`recommended.html`)
        - 사용자가 인증이 되어 있다면, 알고리즘을 활용하여 10개의 영화를 추천하여 제공
        - 알고리즘
            - 사용자에게 genre를 선택할 수 있는 select 옵션을 줍니다.
            - 사용자가 genre를 선택하면 해당 genre의 영화를 10개 이하 출력

- view함수

```python
@require_http_methods(['GET', 'POST'])
def recommended(request):
    if request.method == "POST":
        genre = Genre.objects.get(name=request.POST.get('name'))
        movies = Movie.objects.filter(genres=genre.pk)
    else: 
        movies = None
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/recommended.html', context)
```

GET과 POST 요청을 받아 처리를 다르게 함  
GET일 경우 movies에 None을 반환하고, POST일 경우 request에 있는 장르 이름 데이터를 활용하여 선택된 장르에 해당하는 영화 쿼리셋을 반환
- 초기 페이지: 장르 select form 및 안내 문구 출력 (movies 쿼리셋이 없는 상태)
- 장르 선택시: 장르 select form 출력하여 장르 변경 가능하게 함, 선택한 장르의 영화 목록을 출력 (movies 쿼리셋이 있는 상태)

-------------------------------
### 추천 알고리즘 구현

HTML의 select-option 을 이용하여 구현을 진행함.    
form 태그의 'name'과 views를 연결하여 진행  

```py
if request.method == "POST":
        genre = Genre.objects.get(name=request.POST.get('name'))
```

N:M 관계가 정확히 이해되지 않아 get메서드를 두 번 사용.  

해당 데이터 장르 데이터를 이용하여 이를 render로 전달 후 처리.

---------------------------------
이번 프로젝트에는 보이는 것에 신경을 많이 썼다.
프론트에 가야 하나 싶을 정도로 재미있게 진행했다.
폰트 설정과 카드 배치 등이 조금 까다로웠지만, 노력 끝에 원하는 페이지를 만들 수 있었다. ^___^