<!-- 사전... 설정... -->
In [1]: from movies.models import Movie

In [2]: Movie.objects.all()
Out[2]: <QuerySet [<Movie: 1번째 영화 - 스즈메(애니)>, <Movie: 2번째 영화 - 주술회전(십덕)>, <Movie: 3번째 영화 - 이누야샤(틀뜨억)>]>

In [3]: Movie.objects.all().order_by('id')
Out[3]: <QuerySet [<Movie: 1번째 영화 - 스즈메(애니)>, <Movie: 2번째 영화 - 주술회전(십덕)>, <Movie: 3번째 영화 - 이누야샤(틀뜨억)>]>
<!-- /////////////////////////////////////////////// -->

<!-- 3-2 Todo -->
1. ORM 문법을 사용하여 model의 전체 쿼리셋을 id에 대해 내림차순으로 조회
* In [7]: Movie.objects.all().order_by('-id')
* Out[7]: <QuerySet [<Movie: 3번째 영화 - 이누야샤(틀뜨억)>, <Movie: 2번째 영화 - 주술회전(십덕)>, <Movie: 1번째 영화 - 스즈메(애니)>]>


2. ORM 문법을 사용하여 model의 전체 쿼리셋 중 genre가 action인 것만 조회
* https://lar542.github.io/Django/2019-06-21-first-django-project4/
* In [8]: Movie.objects.filter(genre='action').values()
  * values() 로 하면 리스트 형식으로 반환함
* Out[8]: <bound method QuerySet.values of <QuerySet []>>
* In [11]: Movie.objects.filter(genre='틀뜨억')
* Out[11]: <QuerySet [<Movie: 3번째 영화 - 이누야샤(틀뜨억)>]>


3. ORM 문법을 사용하여 model의 전체 쿼리셋 중 title이 e로 끝나는 것만 조회
* In [13]: Movie.objects.filter(title__endswith='e')
* Out[13]: <QuerySet []>

* In [14]: Movie.objects.filter(title__endswith='샤')
* Out[14]: <QuerySet [<Movie: 3번째 영화 - 이누야샤(틀뜨억)>]>
