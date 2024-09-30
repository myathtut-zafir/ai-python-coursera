# from sentiment_analysis import sentiment_analyzer
import requests

def sentiment_analyzer(text):
    info={
        "URL": 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict',
"Headers": {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"},
"input_json": { "raw_document": { "text": text}, }

}
    
    url = info["URL"]
    headers = info["Headers"]
    myobj = info['input_json']
    response = requests.post(url, json = myobj, headers=headers)
    return response.text
print(sentiment_analyzer("love"))