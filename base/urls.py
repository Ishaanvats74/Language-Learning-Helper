from django.urls import path
from . import views 


urlpatterns = [
    path('',views.Home , name="Home"),
    path('About_us/<str:pk>/',views.About_us , name="About us"),
]