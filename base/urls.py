from django.urls import path
from . import views 


urlpatterns = [
    path('',views.Home , name="Home"),
    path('About_us/',views.About_us , name="About us"),
    path('Translator/',views.Translator , name="Translator"),
    path('Dashboard/',views.Dashboard , name="Dashboard"),
]