from django.urls import path
from . import views

urlpatterns = [
  # path(),
  path('register/', views.register, name='register'),
  path('post/<int:pk>/', views.postDetail, name='postDetail'),
]