from django.urls import path
app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
]
