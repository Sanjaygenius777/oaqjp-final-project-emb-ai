from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("EmotionDetector")

@app.route('/emotionDetector')
def emotion_detect():
    text=request.args.get('textToAnalyze')

    response=emotion_detector(text)
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dominantEmotion=response['dominant_emotion']

    if dominantEmotion is None:
        returnText="Invalid text! Please try again!"
    else:
        returnText=(f"For the given statement, the system response is 'anger': {anger},"
                    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
                    f"The dominant emotion is {dominantEmotion}.")

    return returnText


@app.route('/')
def render_index_page():
    return render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000')