from django.shortcuts import render
import requests

def get_languages():
    url = "https://microsoft-translator-text.p.rapidapi.com/languages"
    querystring = {"api-version": "3.0"}
    headers = {
        "X-RapidAPI-Key": "ca96b4d48emsh41d9e7d659a1317p15cb7ajsnc295d89daab6",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()["translation"]
    return {info["name"]: code for code, info in data.items()}

LANGUAGES = get_languages()

def translate_view(request):
    translated_text = ""
    selected_from = "English"
    selected_to = "Hindi"
    input_text = ""

    if request.method == "POST":
        input_text = request.POST.get("text")
        selected_from = request.POST.get("from_lang")
        selected_to = request.POST.get("to_lang")
        from_code = LANGUAGES[selected_from]
        to_code = LANGUAGES[selected_to]
        translated_text = translate_text(input_text, from_code, to_code)

    return render(request, "base/index.html", {
        "languages": LANGUAGES.keys(),
        "translated_text": translated_text,
        "selected_from": selected_from,
        "selected_to": selected_to,
        "input_text": input_text,
    })

def translate_text(text, from_code, to_code):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {
        "to": to_code,
        "from": from_code,
        "api-version": "3.0"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    body = [{"Text": text}]
    response = requests.post(url, headers=headers, params=querystring, json=body)
    return response.json()[0]["translations"][0]["text"]


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


