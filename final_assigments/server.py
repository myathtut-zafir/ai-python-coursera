''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import render_template,request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
from flask import Flask, make_response
import json
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text=request.args.get("textToAnalyze")
    response=sentiment_analyzer(text)
     # Extract the label and score from the response
    label = response['label']
    score = response['score']
    if label==None:
        return "Invalid input ! Try again."
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO

    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)