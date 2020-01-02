import requests
import json

# Text received from Flask
def language_detector(text_data):
    api_key = "https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20191228T162619Z.ae9fac5e3ce7b128.b8cc7b5dc723af948a8aabe275072026880e09eb"
    url = api_key + "&text=" + text_data
    # Python API call to Flask
    response = requests.get(url)
    # Converting data to JSON format
    result = json.loads(response.text)
    # MAtching language code with the user's language input
    language_dict = {'ta': 'Tamil', 'hi': 'Hindi', 'te': 'Telugu', 'kn': 'Kannada', 'en': 'English'}
    # Checking whether language is available
    if ('lang' in result.keys()) and (result['lang'] != ""):
        lang = result['lang']
        return language_dict[lang]
    else:
        return "Can't detect the language"

