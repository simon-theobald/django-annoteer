# dataitem/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.dataitem_detail, name='dataitem_detail'),
]
