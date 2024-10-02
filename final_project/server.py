'''
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''

from flask import Flask, render_template, request  # Corrected import order and grouped imports
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Receives text from HTML interface and runs sentiment analysis."""
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)

    if response['joy'] is None:  # Changed to use 'is None'
        return "Invalid input! Try again."

    # Formatted response using f-string
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """Renders the main application page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
