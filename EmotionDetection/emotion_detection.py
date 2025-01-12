''' This is a emotion detection Application '''
import requests   # Import the requests library to handle the HTTP requests
import json

def emotion_detector(text_to_analyze):
    ''' This function uses Emotion Predict function of Watson NLP for detecting emotions'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # set the headers for the API request
    myobj = { "raw_document": { "text": text_to_analyze } }    # Create dictionary with the text to be analyzed
    response = requests.post(url,json = myobj, headers = header)   # Send a POST request to the API with the text and header

    response_dict = json.loads(response.text)      # Convert the response text into a dictionary

    emotion_dict = response_dict['emotionPredictions'][0]['emotion']  #extract the emotions and scores

    dominant_emotion = decide_emotion(emotion_dict)  #detect the dominant emotion
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict     #return the emotion detected response

def decide_emotion(dict):
    ''' This function detects dominant emotion based on the scores '''
    max_score = 0
    max_emotion = 'None'
    for emotion in dict:
        if dict[emotion] > max_score:
            max_score = dict[emotion]
            max_emotion = emotion

    return max_emotion


