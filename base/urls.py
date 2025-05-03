from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About_us, name='about_us'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('translator/', views.translator_view, name='translator'),
    path('text-to-speech/', views.my_view, name='text_to_speech'),
]