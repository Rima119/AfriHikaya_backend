from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('refresh/', views.refresh, name='refresh'),
    path('create/', views.create, name='create'),
]
