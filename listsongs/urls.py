from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('get/list/', views.getSongs, name="GetSongs"),
]
