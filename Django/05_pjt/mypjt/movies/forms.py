from django.forms import ModelForm, NumberInput 
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description', 'actor_image']

        widgets ={
            'score': NumberInput(attrs={'min':0, 'max':5, 'step':0.5}),
        }

        label = {
            'title':'제목', 
            'audience':'관객 수', 
            'release_date':'개봉일', 
            'genre':'장르', 
            'score':'평점', 
            'description':'줄거리', 
        }

