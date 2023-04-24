from rest_framework import serializers
from .models import Music, Review


# 문제 1. title 과 release_date 정보만 보이게 MusicListSerializer를 수정하시오.
class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ['title','release_date',] #모든 정보들이 아닌 title과 release_date만 담겨지게


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'



# 문제 6. 리뷰 정보와 N:1 관계를 갖고 있는 Music 의 모든 정보를 music 필드에 나타낼 수 있도록 아래 클래스에 추가하시오.
# 이 때, music 필드는 읽기 전용(read_only)이 되도록 설정합니다.
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__' #모든 정보 포함
        read_only_fields=['music',] #읽기 전용 필드


#reviewSerializer을 적용하기 위해 문제 6과 문제 11 위치 바꿈
# 문제 11. 각 음악 정보에 몇 개의 리뷰가 있는지 확인할 수 있도록 review_count 필드를 아래 클래스에 추가하시오. 
# 이 때, review_count 필드는 읽기 전용(read_only)이 되도록 설정합니다.
class MusicReviewCntSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True) #읽기 전용
    
    class Meta:
        model = Music
        fields = '__all__'