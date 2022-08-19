from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('boards/', views.new_topic),
    path('boards/<int:board_id>/', views.boards_topics, name = 'boards_topics'),
    path('boards/<int:board_id>/new/', views.new_topic, name = 'new topic'),
]

