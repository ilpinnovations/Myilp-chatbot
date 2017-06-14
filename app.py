import urllib
import json
import os


from pprint import pprint
from flask import Flask
from flask import request
from flask import make_response
from flask import url_for
from flask import redirect
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
data_file =  open('sample.json')    
data = json.load(data_file)

@app.route('/', methods=['GET'])
def root():
	return "Sample webhook to connect to api.ai chatbot."

@app.route('/webhook', methods=['POST'])
def webhook():
   
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



   
def makeWebhookResult(req):
    #speech="hi"
    speech = "Something went to Wrong ! Try again Later"
    action = req.get("result").get("action")
    result = req.get("result")
    parameters = result.get("parameters")
    temp_speech=parameters.get("Parameters")
    #if temp_speech=="contact-query":
	 #contact_issue= parameters.get("Contact-Issues")
	 #speech=data["query"][0][temp_speech][contact_issue]
    #else:
    speech=data["query"][0][temp_speech]
    
    

    return {
        "speech": speech,
        "displayText": speech
    }

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
