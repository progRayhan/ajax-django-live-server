from django.urls import path
from display import views as display

urlpatterns = [
    path('', display.home, name="home"),
    path('ajax/getUsers', display.getUsers, name="getUsers"),
]