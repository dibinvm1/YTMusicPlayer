from django.urls import path, include
from player import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('player/',views.player,name='player'),
]
