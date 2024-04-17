from django.urls import path
from . import views

urlpatterns = [
  path('', views.postList, name='postList'),
  path('register/', views.register, name='register'),
  path('post/<int:pk>/', views.postDetail, name='postDetail'),
  path('post/<int:pk>/publish/', views.postPublish, name='postPublish'),  
  path('post/new/', views.postNew, name='postNew'),
]
