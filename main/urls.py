from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('login', views.login),
    # path('', views.login),
    path('profile', views.profle),
    path('index',views.index)
]


