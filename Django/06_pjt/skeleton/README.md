## pjt 06. 관계형 데이터베이스 설계

----
* accounts 앱 생성, mypjy의 settings.py와 urls.py에 accounts 등록
  
----
### 공통 요구사항
#### A. Movie
* 모델 클래스 생성. user_id 외래 키 user 클래스 참조 시 settings import 필요함
#### B. Comment
* user 클래스 참조와 다르게 movie 클래스는 내가 만든 클래스라 settings 불필요
#### C. User
* AbstractUser를 활용하여 클래스 생성. accounts 앱의 models.py에 생성. settings에 AUTH_USER_MODEL 생성해 주어야 함
* 있는 테이블이 없는데도 에러가 뜸... 스켈레톤 코드...    
``` You are trying to add a non-nullable field 'user_id' to movie without a default; we can't do that (the database needs something to populate existing rows).```    
-> null 설정이나 default 설정을 해 주지 않았으면 뜨는 게 당연함. 데이터가 없으면 그냥 아무거나 1 1 설정해 주고 진행

----
### Model
#### A. movie_like_users
* movie_id, user_id를 저장

#### B. user_followings
* accounts 앱의 models.py의 User 클래스에 followings 추가
user_id를 저장(팔로워, 팔로잉 두 칼럼)

![ERD](zmedia\ERD.png)

----
### URL
#### A. movies
* 스켈레톤 코드에 있던 url 외에도 comments, comeents/delete, likes 추가
#### B. accounts 
* urls.py 생성
* login, logout, signup, delete, update, password, profile, follow 추가
  
----
### View
#### A. movies
* 스켈레톤 코드에 있던 view 외에도 comments_create, comments_delete, likes 추가
* 영화 생성 시 user_id와 movie_like_user 필드가 필수로 요구됨 
  * user_id : id는 foriegnkey에서 자동으로 생성해 주는데 필드명을 user로 했어야 함
  * movie_like_user: blank = True 넣어줌. (Null은 db 문제고 blank는 입력 문제)
#### B. accounts
* login, logout, signup, update, delete, chage_password, profile, follow 추가
  
----
### Admin
* Movie, Account 앱의 admin.py에서 Movie, Comment, User을 admin에 등록
* 데이터의 생성, 조회, 수정, 삭제 가능

----
### Form 
#### A. Movie & Comment 모델
* 적절한 ModelForm 사용
* MovieForm은 스켈레톤 코드 그대로 사용
#### B. User 모델
* forms.py 생성
* user CreationForm, ChangeForm 사용

----
### Template
주어진 템플릿 파일들 생성
#### A. base.html
* nav바 생성, 로그인/비로그인 상태에 따른 화면 표시
  * 로그인: 회원정보수정, 로그아웃, 회원탈퇴, 내 프로필
  * 비로그인: 로그인, 회원가입
#### B. index.html
* 전체 영화 목록 조회 페이지
* 영화의 타이틀 클릭 시 detail로 이동
* 좋아요 버튼 생성
* 좋아요 취소가 안 됨-> url.py의 int:pk 수정
* 자동으로 좋아요된 상태로 생성됨 -> index.html에서 ```if request.user in movie.like_users.all ```의 좋아요 취소, 좋아요 상태를 반대로 해 뒀음... DB는 정상이었다

#### C. detail.html
* ```if request.user == movie.user```를 통해 글 작성자만 수정,삭제 가능
* Comments 부분을 통해 댓글 달기 가능
  * 자신의 댓글만 삭제 가능
  * 로그인한 사람만 댓글 등록 가능

#### D. create.html
* 비로그인 상태로 글 create 클릭 시 로그인 페이지 로드 -> view에 if request.user.is_authenticated 추가함

#### E. update.html
* 특정 영화를 수정하기 위한 HTML form 요소 표시

#### F. login.html
* authenticationform을 활용
  
#### G. signup.html
* customusercreationform을 활용

#### H. update.html
* customuserchangeform을 활용

#### I. change_password.html
* passwordchangeform을 활용

#### J. 추가 필수 요구사항
* 로그인한 회원만 영화 정보 touch 가능 ㅇ
* 본인의 영화만 수정,삭제 가능 ㅇ
* 로그인한 회원만 댓글 생성,삭제 가능 ㅇ
* 본인의 댓글만 삭제 가능 ㅇ
* 비밀번호 변경 직후 로그인 상태 유지 ㅇ
* 본인 팔로우 불가 ㅇ