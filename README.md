# Translation - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Translation API](https://www.ai-compare.com/text_apis/automatic_translation/). [AI-Compare Translation API](https://www.ai-compare.com/text_apis/automatic_translation/) allows to call Translation APIs from Google Cloud Platform Translate, AWS Translate, Microsoft Azure Cognitives Service Language, and IBM Watson Natural Language Translation. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/text/automatic_translation'
```
### Select parameters 
Set your text, the source and target language, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_to_translate':'how are you today', 'source_language': 'en','target_language': 'fr'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
{"result": [{"solution_name": "Ibm","execution_time": "7.103219","result": {"source_language": "English","target_language": "French","translated_text": "Le score d'un sentiment de documents indique l'émotion générale d'un document. L'ampleur du sentiment des documents indique la quantité de contenu émotionnel présente dans le document, et cette valeur est souvent proportionnelle à la longueur du document."},"api_response": {"translations": [{"translation": "Le score d'un sentiment de documents indique l'émotion générale d'un document. L'ampleur du sentiment des documents indique la quantité de contenu émotionnel présente dans le document, et cette valeur est souvent proportionnelle à la longueur du document."}],"word_count": 41,"character_count": 255}},{"solution_name": "Microsoft Azure","execution_time": "1.538659","result": {"source_language": "English","target_language": "French","translated_text": "La partition d’un sentiment de documents indique l’émotion globale d’un document. L’ampleur d’un sentiment de documents indique combien de contenu émotionnel est présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document."},"api_response": [{"detectedLanguage": {"language": "en","score": 1},"translations": [{"text": "La partition d’un sentiment de documents indique l’émotion globale d’un document. L’ampleur d’un sentiment de documents indique combien de contenu émotionnel est présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document.","to": "fr"}]}]},
```

</summary>

```json
{
  "result": [
    {
      "solution_name": "Ibm",
      "execution_time": "7.103219",
      "result": {
        "source_language": "English",
        "target_language": "French",
        "translated_text": "Le score d'un sentiment de documents indique l'émotion générale d'un document. L'ampleur du sentiment des documents indique la quantité de contenu émotionnel présente dans le document, et cette valeur est souvent proportionnelle à la longueur du document."
      },
      "api_response": {
        "translations": [
          {
            "translation": "Le score d'un sentiment de documents indique l'émotion générale d'un document. L'ampleur du sentiment des documents indique la quantité de contenu émotionnel présente dans le document, et cette valeur est souvent proportionnelle à la longueur du document."
          }
        ],
        "word_count": 41,
        "character_count": 255
      }
    },
    {
      "solution_name": "Microsoft Azure",
      "execution_time": "1.538659",
      "result": {
        "source_language": "English",
        "target_language": "French",
        "translated_text": "La partition d’un sentiment de documents indique l’émotion globale d’un document. L’ampleur d’un sentiment de documents indique combien de contenu émotionnel est présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document."
      },
      "api_response": [
        {
          "detectedLanguage": {
            "language": "en",
            "score": 1
          },
          "translations": [
            {
              "text": "La partition d’un sentiment de documents indique l’émotion globale d’un document. L’ampleur d’un sentiment de documents indique combien de contenu émotionnel est présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document.",
              "to": "fr"
            }
          ]
        }
      ]
    },
    {
      "solution_name": "Amazon Web Services",
      "execution_time": "1.161538",
      "result": {
        "source_language": "English",
        "target_language": "French",
        "translated_text": "Le score d'un sentiment de documents indique l'émotion globale d'un document. L'ampleur d'un sentiment de document indique la quantité de contenu émotionnel présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document."
      },
      "api_response": {
        "TranslatedText": "Le score d'un sentiment de documents indique l'émotion globale d'un document. L'ampleur d'un sentiment de document indique la quantité de contenu émotionnel présent dans le document, et cette valeur est souvent proportionnelle à la longueur du document.",
        "SourceLanguageCode": "en",
        "TargetLanguageCode": "fr",
        "ResponseMetadata": {
          "RequestId": "419bad32-d26b-458d-9eb3-967ce0c53546",
          "HTTPStatusCode": 200,
          "HTTPHeaders": {
            "x-amzn-requestid": "419bad32-d26b-458d-9eb3-967ce0c53546",
            "cache-control": "no-cache",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "331",
            "date": "Wed, 13 May 2020 15:38:30 GMT"
          },
          "RetryAttempts": 0
        }
      }
    }
  ]
}
```

</details>

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for NLP APIs](https://www.ai-compare.com/use_cases_nlp/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)
