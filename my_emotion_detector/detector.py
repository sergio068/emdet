from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_predictor(text):
    try:
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2018-11-16',
            iam_apikey='YOUR_API_KEY',
            url='https://gateway.watsonplatform.net/natural-language-understanding/api'
        )
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        emotions = response['emotion']['document']['emotion']
        formatted_response = {
            'text': text,
            'emotions': emotions
        }
        return formatted_response
    except Exception as e:
        return {'error': str(e)}, 500

