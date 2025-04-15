from django.shortcuts import render
from .models import About_US
# Create your views here.
# details = [
#     {'id':1 , 'name' : 'Lets! learn Python'},
#     {'id':2 , 'name' : 'Lets! learn JavaScript'},
#     {'id':3 , 'name' : 'Lets! learn Css'},
# ]


def Home(request):
    details = About_US.objects.all()
    context = {'details':details}
    return render(request,'base/home.html' , context)

def About_us(request):
    About_us = About_US
    context = {'About_us' : About_us}
    return render(request,'base/about_us.html',context)

def Translator(request):
   
    context = {'Translator' : Translator}
    return render(request,'base/translatorPage.html',context)

def Dashboard(request):
    
    context = {'Dashboard' : Dashboard}
    return render(request,'base/dashboardPage.html',context)    


