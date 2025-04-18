from django.shortcuts import render




def Home(request):
    context = {'Home':Home}
    return render(request,'base/home.html' , context)

def About_us(request):

    context = {'About_us' : About_us}
    return render(request,'base/about_us.html',context)

def Translator(request):
   
    context = {'Translator' : Translator}
    return render(request,'base/translatorPage.html',context)

def Dashboard(request):
    
    context = {'Dashboard' : Dashboard}
    return render(request,'base/dashboardPage.html',context)    


