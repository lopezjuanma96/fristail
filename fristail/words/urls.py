from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('random/<str:language>/', views.random, name='random'),
]
