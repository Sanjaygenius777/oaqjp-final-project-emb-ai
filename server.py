"""Final Project of Emotion Detection for pyhton flask and api"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("EmotionDetector")

@app.route('/emotionDetector')
def emotion_detect():
    """ This is route handler function to return result of emotion detection done by the model """
    text=request.args.get('textToAnalyze')

    response=emotion_detector(text)
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dominant_emotion=response['dominant_emotion']

    if dominant_emotion is None:
        return_text="Invalid text! Please try again!"
    else:
        return_text=(f"For the given statement, the system response is 'anger': {anger},"
                    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
                    f"The dominant emotion is {dominant_emotion}.")

    return return_text


@app.route('/')
def render_index_page():
    """This route renders the html template"""
    return render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000')
