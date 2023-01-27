# 02. PJT_readme - 1반 이예슬


### 0. 공통 요구사항
* API 요청 시 언어 및 지역 설정은 한국 기준
  * ```params```에 ```'language':'ko', 'region':'KR'``` 추가해 주었음
-------
### 1. problem a
* 최소 조건
  * ```response```리스트에 ```get Popular``` URL을 통해 1페이지의 데이터 request
  * ```count``` 변수를 생성하여 for문(```response``` 조회)을 통해 요소 개수 카운트
--------
### 2. problem b
* 최소 조건
  * ```response```리스트에 ```get Popular``` URL을 통해 1페이지의 데이터 request
  * ```over8``` 리스트를 생성하여 for문(```response``` 조회) 내 if문을 통해 ```vote_average```가 8점 이상인 영화 정보만 ```over8```에 append
* 오류
  * 공통 요구사항을 제대로 읽지 않아 ```region``` 설정을 뒤늦게 했음
--------
### 3. problem c
* 최소 조건
  * ```response```리스트에 ```get Popular``` URL을 통해 1페이지의 데이터 request
  * ```rank5``` 리스트를 생성하여 for문(```response``` 조회)을 통해 ```title```과 ```vote_average```만 append
  * sort를 통해 ```vote_average```기준 정렬
  * 이후 5번째까지의 값만 다시 ```rank5```에 저장
  * ```answer``` 리스트를 생성하여 이중for문을 통해 ```response```의 ```title```과 ```rank5```의 0번째 인덱스값이 같을 때의 ```response```의 요소 append
* 오류
  * list의 인덱스에 따른 sort 방법을 몰라 구글링. 람다 함수의 활용법에 익숙해질 필요가 있음
--------
### 4. problem d
* 최소 조건
  * ```response```리스트에 ```Search Movies``` URL을 통해 1페이지의 데이터 request
  * if :```response```의 len()이 0일 때는 검색한 영화 정보가 없는 것이니 ```None``` 반환
  * elif 조건: ```response```의 첫번째 값의 ```id```가 int형일 때
    * ```id```변수에 조건식의 값을 할당하고, 이를 활용하여 ```rec_response``` 변수에 ```Get Recommendations``` 데이터 request
    * for문(```rec_response```  조회)을 통해 ```title``` 리스트에 ```rec_response``` 요소의 ```title```만 append
  * elif 조건에 맞지 않으면 추천 영화가 없다는 것, 따라서 빈 리스트인 ```title```을 반환 ->```[]``` 
--------
### 5. problem e
* 최소 조건
  * ```response```리스트에 ```Search Movies``` URL을 통해 1페이지의 데이터 request
  * if :```response```의 len()이 0일 때는 검색한 영화 정보가 없는 것이니 ```None``` 반환
  * elif 조건: ```response```의 첫번째 값의 ```id```가 int형일 때
    * ```id```변수에 조건식의 값을 할당하고, 이를 활용하여 ```rec_response``` 변수에 ```Get Recommendations``` 데이터 request
    * ```cast``` 변수에 ```cast```의 데이터를, ```direct``` 변수에 ```crew```의 데이터를 request
    * ```castname``` 리스트를 생성하여 for문(```cast``` 조회)을 통해 ```department```가 10 미만인 ```cast```의 ```original_name```만 append
    * ```directname``` 리스트를 생성하여 for문(```direct``` 조회)을 통해 ```cast_id```가 'Directing'인 ```direct```의 ```original_name```만 append
--------
