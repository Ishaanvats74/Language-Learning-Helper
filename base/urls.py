from django.urls import path
from . import views
from .views import translator_view  

urlpatterns = [
    path('', views.Home, name="Home"),
    path('About_us/', views.About_us, name="About us"),
    path('Translator/', views.Translator, name="Translator"),
    path('Dashboard/', views.Dashboard, name="Dashboard"),
    path('translator-form/', translator_view, name="translator_form"),  
]
