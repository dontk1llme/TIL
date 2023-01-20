# 01. PJT_readme - 1반 이예슬


### 1. problem a
* 최소 조건
  * ```movie_info```내 ```new_data``` 라는새로운 딕셔너리를 생성.
  * ```movie.json```에서 필요한 정보들만 추출하여 저장.
  * ```movie_info(movie)```를 실행하게 되면 추출된 정보만 보여줌.  
* 추가
  * ```pprint```의 첫 사용.
  * get을 여러번 반복하는데 이걸 쉽게 하는 방법?
------------------
### 2. problem b
* 최소 조건
  * ```problem a```에서 만들었던 ```movie_info``` 내의 ```genre_ids```를 ```genre_names```로 변경하기로 설정.
  * 장르들의 이름을 담을 ```newls``` 리스트 생성.
  * 원래 사용했던 ```genre_ids```와 ```generes```내의 ```id```가 일치하면 ```name```을 ```newls```에 ```append```.
  * 그렇게 생성된 ```newls```는 ```genre_names```의 값이 됨.
--------------------
### 3. problem c
* 최소 조건
  * 이전 단계의 함수 구조 재사용 (```problem b```의 구조 재사용)
  * ```problem b```의 ```movie_info``` 함수의 return값을 ```mvlst``` 변수에 저장하여 return함.
  * 원래 1개의 dict였던 ```movie```가 여러 개의 list 형식으로 반환된 부분을 중점으로 코드 수정.
* 오류
  *  for문에 i를 쓰는 것이 습관인데 이 때문에 i가 꼬여서 조금 시간을 낭비함.
---
### 4. problem d
* 최소 조건
  * 설계
    * for문을 통해 ```movies```의 ```id```와 파일명이 일치하는 json파일을 로드.
    * json파일의 ```title```과 ```revenue```를 저장하는 ```lst``` 리스트 생성
    * ```lst```를 ```revenue``` 기준 내림차순 정렬하여 첫 번째 인덱스 ```title``` 반환
  * 오류
    * 내림차순 정렬과 오름차순 정렬을 하는 것이 헷갈린다. 인덱스와 -, lambda식 활용 연습이 필요한 것 같다.
      * [sorting](https://docs.python.org/3/howto/sorting.html) 에서 ```key``` 검색하여 활용
---
### 5. problem e
* 최소 조건
* 설계 
  * ```problem d```와 비슷한 형식으로 진행
  * for문을 통해 ```movies```의 ```id```와 파일명이 일치하는 json파일을 로드.
  * json파일의 ```title```을 저장하는 ```lst``` 리스트 생성
    * if ```release_date```: 슬라이싱을 통해 개봉일이 12월인 영화만 append.
  * ```lst```의 첫 번째 인덱스인 ```title```만 반환
* 의문
  * 굳이 ```movies 폴더```를 열지 않아도 ```movies.json``` 파일 내에 필요한 정보가 다 있는데... 영화 하나하나의 파일을 열면 불필요한 처리를 하게 된 게 아닌가?
---
### 6. problem f
1) 90년대 개봉작 중 많은 수입을 올린 영화 순위  
   * ```top_90(movies)``` 함수
     * 설계
     * for문을 통해 ```movies```의 ```id```와 파일명이 일치하는 json파일을 로드.
     * json파일의 ```title```과 ```revenue```를 저장하는 ```lst``` 리스트 생성
       *  if ```release_date```: 슬라이싱을 통해 개봉년이 90년대인 영화만 append.
     *  ```lst```의 첫 번째 인덱스인 ```title```만 반환
2) 배급한 영화가 많은 순으로 배급사 정렬하기  
   * ```top_company(movies)``` 함수
     * 설계
       * for문을 통해 ```movies```의 ```id```와 파일명이 일치하는 json파일을 로드.
       * json파일의 ```production_companies```의 ```name```과을 저장하는 ```lst``` 리스트 생성
       * ```counter``` : [{'회사명', '배급한 영화 수'}, {'회사명', '배급한 영화 수'}, ...]
         * 배급한 영화 수: 회사별로 count가 가능한 조건문 작성
       * ```counter```를 value값 기준으로 정렬, 배급사와 횟수 리턴
  


