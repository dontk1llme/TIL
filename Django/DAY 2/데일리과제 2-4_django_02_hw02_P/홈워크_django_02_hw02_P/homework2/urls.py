from django.urls import path
urlpatterns = [
    path('articles/', include('articles.urls'),
    path('pages/', include('pages.urls'),
]
