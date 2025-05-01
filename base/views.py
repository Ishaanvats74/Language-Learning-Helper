import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import json

# Your API key (consider moving this to settings.py)
RAPIDAPI_KEY = "ca96b4d48emsh41d9e7d659a1317p15cb7ajsnc295d89daab6"

def get_languages():
    """Fetch available languages from Microsoft Translator API"""
    url = "https://microsoft-translator-text.p.rapidapi.com/languages"
    querystring = {"api-version": "3.0"}
    headers = {
        "x-rapidapi-host": "microsoft-translator-text.p.rapidapi.com",
        "x-rapidapi-key": RAPIDAPI_KEY,
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        languages = data.get("translation", {})
        return [(code, info["name"]) for code, info in languages.items()]
    except Exception as e:
        print(f"Error fetching languages: {e}")
        # Fallback to common languages if API fails
        return [
            ('en', 'English'),
            ('es', 'Spanish'),
            ('fr', 'French'),
            ('de', 'German'),
            ('it', 'Italian'),
            ('zh-Hans', 'Chinese (Simplified)'),
            ('ja', 'Japanese'),
            ('ko', 'Korean'),
            ('ru', 'Russian'),
            ('ar', 'Arabic'),
            ('hi', 'Hindi'),
            ('pt', 'Portuguese')
        ]


def translator_view(request):
    """Main translation view without JavaScript dependencies"""
    # Default values
    languages = get_languages()
    translated_text = ""
    from_lang = "en"  # Default from language
    to_lang = "es"    # Default to language
    input_text = ""
    
    # Process translation request
    if request.method == "POST":
        action = request.POST.get('action', 'translate')
        
        # Handle different form actions
        if action == 'translate':
            from_lang = request.POST.get("from_lang", "en")
            to_lang = request.POST.get("to_lang", "es")
            input_text = request.POST.get("input_text", "").strip()
            
            # Only call API if there's text to translate
            if input_text:
                try:
                    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
                    querystring = {
                        "to": to_lang,
                        "api-version": "3.0",
                        "from": from_lang,
                        "profanityAction": "NoAction",
                        "textType": "plain"
                    }
                    
                    payload = [{"Text": input_text}]
                    headers = {
                        "content-type": "application/json",
                        "X-RapidAPI-Key": RAPIDAPI_KEY,
                        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
                    }
                    
                    response = requests.post(url, json=payload, headers=headers, params=querystring)
                    response.raise_for_status()
                    
                    result = response.json()
                    print(f"API Response: {json.dumps(result, indent=2)}")
                    
                    if result and len(result) > 0:
                        translated_text = result[0]["translations"][0]["text"]
                    else:
                        messages.error(request, "No translation returned")
                
                except requests.exceptions.RequestException as e:
                    print(f"API Request Error: {e}")
                    messages.error(request, "Translation API request failed. Please try again later.")
                
                except (KeyError, IndexError, json.JSONDecodeError) as e:
                    print(f"Response parsing error: {e}")
                    messages.error(request, "Could not process translation response.")
                
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    messages.error(request, "An unexpected error occurred.")
        
        elif action == 'swap_languages':
            # Handle language swap action
            from_lang = request.POST.get("to_lang", "es")
            to_lang = request.POST.get("from_lang", "en")
            input_text = request.POST.get("input_text", "")
            translated_text = request.POST.get("translated_text", "")
            
            # Swap the input and translated text
            input_text, translated_text = translated_text, input_text
        
        elif action == 'copy_text':
            # We'll handle copying on the frontend with minimal JS
            # Just return the same form data
            from_lang = request.POST.get("from_lang", "en")
            to_lang = request.POST.get("to_lang", "es")
            input_text = request.POST.get("input_text", "")
            translated_text = request.POST.get("translated_text", "")
            messages.success(request, "Text copied to clipboard!")
    
    # Prepare context for the template
    context = {
        "languages": languages,
        "translated_text": translated_text,
        "from_lang": from_lang,
        "to_lang": to_lang,
        "input_text": input_text,
    }
    
    return render(request, "base/translatorPage.html", context)


def Home(request):
    """Home page view"""
    return render(request, 'base/home.html', {})


def About_us(request):
    """About us page view"""
    return render(request, 'base/about_us.html', {})


def Dashboard(request):
    """Dashboard page view"""
    return render(request, 'base/dashboardPage.html', {})