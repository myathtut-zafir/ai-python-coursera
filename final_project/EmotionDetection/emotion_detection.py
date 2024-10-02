import requests
import json

def emotion_detector(text_to_analyze):
    info = {
        "URL": 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        "Headers": {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        "input_json": {"raw_document": {"text": text_to_analyze}}
    }
    
    url = info["URL"]
    headers = info["Headers"]
    myobj = info['input_json']
    
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_data = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
            'dominant_emotion': '<name of the dominant emotion>'
        }

        # Determine dominant emotion
        dominant_emotion = max((key for key in emotion_data if isinstance(emotion_data[key], (int, float))), key=emotion_data.get)
        emotion_data['dominant_emotion'] = dominant_emotion
    
    else:
        # Handle error or invalid response
        emotion_data = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return emotion_data
