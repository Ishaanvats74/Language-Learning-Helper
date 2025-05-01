from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('About_us/', views.About_us, name="About us"),
    path('Dashboard/', views.Dashboard, name="Dashboard"),
    path('translator_form/', views.translator_view, name="translator_form"),  
]
