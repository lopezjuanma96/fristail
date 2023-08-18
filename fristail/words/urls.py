from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('random/<str:language>/', views.random, name='random'),
]
