## 1. 프로젝트 목표

- DRF를 활용한 API Server 제작
- Database many to one relationship(1:N)에 대한 이해
- Database many to many relationship(M:N)에 대한 이해

## 2. 개발도구 및 제공사항

- Visual Studio Code
- Google Chrome
- Django 3.2+
- Postman

## 3. 프로젝트 과정

- 가상환경 설정, 활성화 및 패키지 설치
- 모델 생성 및 관계 설정

    1.  Review class 가 Movie class를 1:N 참조
    2.  Movie class 가 Actor class를 N:M 참조 
        - 역참조를 movies로 명명
- 세 개의 모델을 Admin site에 등록하고, 데이터의 생성, 조회, 수정, 삭제

    A. 전체 배우 목록 제공
    
    - serializer.py 작성
        
        ```python
        class ActorSerListializer(serializers.ModelSerializer):
        
            class Meta:
                model = Actor
                fields = '__all__'
        ```
        
        ⇒ serializer class를 통해 데이터를 json 형태로 변환
        
    - views.py 작성
        
        ```python
        @api_view()
        def actor_list(request):
            actors = Actor.objects.all()
            serializers = ActorSerListializer(actors, many=True)
            return Response(serializers.data)
        ```
        
        ⇒ 함수를 정의하여 함수 호출 시 Actor에 담긴 json 파일 모두 가져오기
        
    
    B. 단일 배우 정보 제공
    
    - serializer.py작성
        
        ```python
        class Moivetitle(serializers.ModelSerializer):
        
            class Meta:
                model = Movie
                fields = ('title',)
        
        class ActorSerializer(serializers.ModelSerializer):
            movies = Moivetitle(many=True, read_only=True)
            class Meta:
                model = Actor
                fields = '__all__'
        ```
        
        ⇒ Movie를 역참조하여 title만 가져오기
      
        
    - views.py
        
        ```python
        @api_view()
        def artor_detail(request, actor_pk):
            actor = Actor.objects.get(pk=actor_pk)
            serializers = ActorSerializer(actor)
            return Response(serializers.data)
        ```
        
        ⇒ 키 값에 해당하는 배우의 정보를 출력한다.
        
    
    C.  전체 영화 목록 제공
    
    - serializer.py
        
        ```python
        class MoiveListSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Movie
                fields = ('title', 'overview',)
        ```
        
        ⇒ Movie에서 title 필드와 overviw 필드만 가져와 json 타입으로 반환
        
    
    D. 단일 영화 목록 제공
    
    - serializer.py
        
        ```python
        class Actorname(serializers.ModelSerializer):
        
            class Meta:
                model = Actor
                fields = ('name',)
        
        class MoiveSerializer(serializers.ModelSerializer):
            actors = Actorname(many=True, read_only=True)
            review_set = ReviewListSerializer(many=True, read_only=True)
            class Meta:
                model = Movie
                fields = '__all__'
        ```
        
        ⇒ Actor를 참조하여 name 필드를 가져오고, Review를 역참조하여 title과 content 값을 가져온다.
    
    E. 전체 리뷰 목록 제공
    
    - serializer.py
        
        ```python
        class ReviewListSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Review
                fields = ('title','content',)
        ```

    
    F. 단일 리뷰 조회 & 수정 & 삭제
    
    - serializer.py
        
        ```python
        class ReviewSerializer(serializers.ModelSerializer):
            movie = Moivetitle(read_only=True)
            class Meta:
                model = Review
                fields = '__all__'
        ```
        
        ⇒ Movie를 참조하여 title 필드와  Review의 모든 필드를 json형태로 변환
        
    - views.py
        
        ```python
        @api_view(['GET', 'PUT', 'DELETE'])
        def review_detail(request, review_pk):
            review = Review.objects.get(pk=review_pk)
        
            if request.method == 'GET':
                serializers = ReviewSerializer(review)
                return Response(serializers.data)
            
            elif request.method == 'PUT':
                serializers = ReviewSerializer(review, data=request.data)
                if serializers.is_valid(raise_exception=True):
                    serializers.save()
                    return Response(serializers.data)
            
            elif request.method == 'DELETE':
                review.delete()
                message_d = f'review {review_pk} is deleted'
                return Response(message_d, status=status.HTTP_204_NO_CONTENT)
        ```

    G. 리뷰 생성
    
    - serializer.py ⇒ `ReviewSerializer`
        
    - views.py
        
        ```python
        @api_view(['POST'])
        def create_review(request, movie_pk):
            movie = Movie.objects.get(pk=movie_pk)
            serializers = ReviewSerializer(data=request.data)
            if serializers.is_valid(raise_exception=True):
                serializers.save(movie=movie)
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        ```