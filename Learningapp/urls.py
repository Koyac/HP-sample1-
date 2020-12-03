from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index'),
    path('index/', views.index1, name='index'),
    path('about/', views.about1, name='about'),
    path('gallery/', views.gallery1, name='gallery'),
    path('link/', views.link1, name='link'),
]