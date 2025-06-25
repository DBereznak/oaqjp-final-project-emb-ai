import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=payload, headers=headers)
    raw_data = json.loads(res.text)
    emotion_score = raw_data['emotionPredictions'][0]['emotion']
   # dominent_score = max([emotion_score['anger'], emotion_score['disgust'],emotion_score['fear'], emotion_score['joy'], emotion_score['sadness']]) 
    
    score = 0
    for key, value in emotion_score.items():
        if value > score:
            score = value
            dominent_emotion = key
            
    emotion_analysis = {
        'anger' : emotion_score['anger'],
        'disgust': emotion_score['disgust'],
        'fear': emotion_score['fear'],
        'joy' : emotion_score['joy'],
        'sadness': emotion_score['sadness'],
        'dominent_emotion' : dominent_emotion
    }
    print(emotion_analysis)

emotion_detector("I love this new technology.")