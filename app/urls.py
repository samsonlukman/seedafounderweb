from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('founder/', views.founder, name='founder'),
    path('investor', views.investor, name='investor'),
    path('/experts', views.experts, name='experts')
]