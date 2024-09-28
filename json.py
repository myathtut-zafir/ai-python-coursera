from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    response_data={"message":"Hello World"}
    return jsonify(response_data)