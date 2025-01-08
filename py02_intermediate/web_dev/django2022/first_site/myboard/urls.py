from unicodedata import name
from django.urls import path
from . import views

app_name = 'myboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('answer/create/<int:post_id>/', views.answer_create, name='answer_create'),
    path('post/create/', views.post_create, name='post_create'),
]