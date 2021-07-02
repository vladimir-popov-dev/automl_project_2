# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('lk/', lk_view, name="lk"),
    path('dataset_create/', create_data, name="dataset_create"),

]

