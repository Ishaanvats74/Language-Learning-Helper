import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

RAPIDAPI_KEY = "ca96b4d48emsh41d9e7d659a1317p15cb7ajsnc295d89daab6"

def get_languages():
    url = "https://microsoft-translator-text.p.rapidapi.com/languages"
    querystring = {"api-version": "3.0"}
    headers = {
        "x-rapidapi-host": "microsoft-translator-text.p.rapidapi.com",
        "x-rapidapi-key": RAPIDAPI_KEY,
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    languages = data["translation"]
    return [(code, info["name"]) for code, info in languages.items()]

def translator_view(request):
    languages = get_languages()
    translated_text = ""
    
    if request.method == "POST":
        from_lang = request.POST.get("from_lang")
        to_lang = request.POST.get("to_lang")
        input_text = request.POST.get("input_text")

        url = "https://microsoft-translator-text.p.rapidapi.com/translate"
        querystring = {"to": to_lang, "api-version": "3.0", "from": from_lang}
        payload = [{"Text": input_text}]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
        }
        response = requests.post(url, json=payload, headers=headers, params=querystring)
        translated_text = response.json()[0]["translations"][0]["text"]

    return render(request, "translator.html", {
        "languages": languages,
        "translated_text": translated_text
    })



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


