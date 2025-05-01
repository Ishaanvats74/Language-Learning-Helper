import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import json

# Your API key (consider moving this to settings.py or environment variables for security)
# Make sure this is your current valid RapidAPI key
RAPIDAPI_KEY = "ca96b4d48emsh41d9e7d659a1317p15cb7ajsnc295d89daab6"  # Verify this key is active
RAPIDAPI_HOST = "translateai.p.rapidapi.com"

def get_languages():
    """Return list of supported languages for TranslateAI API"""
    # TranslateAI supports many languages but doesn't have a specific endpoint for listing them
    # Providing common languages based on ISO 639-1 codes
    return [
        ('auto', 'Auto-detect'),
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('zh', 'Chinese (Simplified)'),
        ('ja', 'Japanese'),
        ('ko', 'Korean'),
        ('ru', 'Russian'),
        ('ar', 'Arabic'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        ('pt', 'Portuguese'),
        ('nl', 'Dutch'),
        ('tr', 'Turkish'),
        ('pl', 'Polish'),
        ('uk', 'Ukrainian'),
        ('cs', 'Czech'),
        ('sv', 'Swedish'),
        ('vi', 'Vietnamese'),
        ('th', 'Thai')
    ]


def translator_view(request):
    """Main translation view"""
    # Default values
    languages = get_languages()
    translated_text = ""
    from_lang = "en"  # Default from language
    to_lang = "es"    # Default to language
    input_text = ""
    
    # Process translation request
    if request.method == "POST":
        action = request.POST.get('action', 'translate')
        from_lang = request.POST.get("from_lang", "en")
        to_lang = request.POST.get("to_lang", "es")
        input_text = request.POST.get("input_text", "").strip()
        
        # Handle different form actions
        if action == 'translate':
            # Only call API if there's text to translate
            if input_text:
                try:
                    # Use TranslateAI API
                    url = "https://translateai.p.rapidapi.com/google/translate/json"
                    
                    # Format the origin_language (use "auto" if auto-detect was selected)
                    origin_language = "auto" if from_lang == "auto" else from_lang
                    
                    # Prepare the payload for TranslateAI API
                    payload = {
                        "origin_language": origin_language,
                        "target_language": to_lang,
                        "json_content": {
                            "text": input_text
                        }
                    }
                    
                    headers = {
                        "Content-Type": "application/json",
                        "X-RapidAPI-Key": RAPIDAPI_KEY,
                        "X-RapidAPI-Host": RAPIDAPI_HOST
                    }
                    
                    print(f"Sending request to: {url}")
                    print(f"With headers: {headers}")
                    print(f"With payload: {payload}")
                    
                    # Make the POST request
                    response = requests.post(url, json=payload, headers=headers)
                    
                    # Debug the response
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Headers: {response.headers}")
                    print(f"Response Content: {response.text[:500]}...")  # Print first 500 chars for debugging
                    
                    # Check for HTTP errors
                    response.raise_for_status()
                    
                    # Parse the response
                    result = response.json()
                    
                    # Extract translated text from the TranslateAI response format
                    if result and "translated_json" in result and "text" in result["translated_json"]:
                        translated_text = result["translated_json"]["text"]
                        messages.success(request, "Translation successful!")
                    else:
                        messages.error(request, "No translation returned from API")
                        print(f"Unexpected API response structure: {result}")
                
                except requests.exceptions.RequestException as e:
                    print(f"API Request Error: {e}")
                    messages.error(request, f"Translation API request failed: {str(e)}")
                
                except (KeyError, IndexError, json.JSONDecodeError) as e:
                    print(f"Response parsing error: {e}")
                    print(f"Response content: {response.text if 'response' in locals() else 'No response'}")
                    messages.error(request, f"Could not process translation response: {str(e)}")
                
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    messages.error(request, f"An unexpected error occurred: {str(e)}")

                # If translation failed, translated_text remains empty
                if not translated_text:
                    translated_text = ""
        
        elif action == 'swap_languages':
            # Handle language swap action
            # Swap the languages (don't swap if auto-detect is selected)
            if from_lang != "auto":
                from_lang, to_lang = to_lang, from_lang
            else:
                # If auto-detect was selected, just set from_lang to to_lang
                from_lang = to_lang
                to_lang = request.POST.get("from_lang", "en")
            
            # Also swap the texts if both exist
            if input_text or request.POST.get("translated_text", ""):
                input_text = request.POST.get("translated_text", "")
                translated_text = request.POST.get("input_text", "")
    
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