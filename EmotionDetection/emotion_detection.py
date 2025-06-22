import requests 
import json

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header1={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input1={ "raw_document": { "text": text_to_analyze } }
    response= requests.post(url,headers=header1,json=input1)
    res=json.loads(response.text)
    emotion=res['emotionPredictions'][0]['emotion']
    domkey=''
    maxvalue=0.0
    for key,value in emotion.items():
        if value>maxvalue:
            maxvalue=value
            domkey=key
    
    emotion['dominant_emotion']=domkey
    return emotion