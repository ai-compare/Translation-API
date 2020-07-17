import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#1f5c4e0d-9c1a-4d8f-8c37-19bfdbfcc893

#Enter your API Token
headers = {'x-access-token': 'Enter your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/api/v1/text/create/compare/automatic_translation'

# Select providers, and text to translate, and source / target languages
payload = {'providers': '[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_to_translate':'how are you today', 'source_language': 'en','target_language': 'fr'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
