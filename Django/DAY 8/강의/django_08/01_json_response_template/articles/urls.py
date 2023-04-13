from django.urls import path
from . import views


urlpatterns = [
    # path('html/', views.article_html),
    # path('json-1/', views.article_json_1),
    # path('json-2/', views.article_json_2),
    # path('json-3/', views.article_json_3),
    path('articles/', views.article_list), #템플릿 안 쓸 거니까 name 안줌 일단
    path('articles/<int:article_pk>/', views.article_detail),
    
]
