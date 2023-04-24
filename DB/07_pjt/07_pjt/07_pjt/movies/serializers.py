from rest_framework import serializers

from .models import Movie, Actor, Review

class ActorSerListializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class MoiveListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

class Moivetitle(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class Actorname(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

class ActorSerializer(serializers.ModelSerializer):
    movies = Moivetitle(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

class MoiveSerializer(serializers.ModelSerializer):
    actors = Actorname(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = Moivetitle(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'