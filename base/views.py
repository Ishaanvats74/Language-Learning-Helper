from django.shortcuts import render

# Create your views here.
details = [
    {'id':1 , 'name' : 'Lets! learn Python'},
    {'id':2 , 'name' : 'Lets! learn JavaScript'},
    {'id':3 , 'name' : 'Lets! learn Css'},
]


def Home(request):
    context = {'details':details}
    return render(request,'base/home.html' , context)

def About_us(request,pk):
    About_us = None
    for i in details:
        if i['id'] == int(pk):
            About_us = i 
    context = {'About_us' : About_us}
    return render(request,'base/about_us.html',context)