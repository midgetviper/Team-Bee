import nexmo
from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import json
import requests

client = nexmo.Client(
    key="dummy",
    secret="dummy",
    application_id="b4a98454-b177-4771-b17f-05704996455e",
    private_key="./private.key",
)

app = Flask(__name__)
CORS(app, support_credentials=True)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return "Nexmo Voice"


@app.route('/call/<patient_num>', methods=['GET'])
def call(patient_num):
    response = client.create_call({
        'to': [{'type': 'phone', 'number': patient_num}],
        'from': {'type': 'phone', 'number': 447418340450},
        'answer_url': ['http://3e080526.ngrok.io/ncco']
        })
    return jsonify(response)


@app.route('/ncco', methods=['GET', 'POST'])
def ncco():
    with open('ncco/talk.json') as f:
        ncco = json.loads(f.read())
    return jsonify(ncco)      
    

@app.route('/medtaken', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def medtaken():
    data = request.data
    #print(request.data)
    return "ok"

@app.route('/recording', methods=['GET', 'POST'])
def recording():
    event = request.get_json()
    headers =  client._Client__headers()
    response = requests.get(event['recording_url'], headers=headers)
    with open("./" + event["conversation_uuid"]+".mp3", "wb") as f:
        f.write(response.content)
    return "ok"


@app.route('/event', methods=['GET', 'POST'])
def event():
    print(request.get_json())
    return "ok"


if __name__ == '__main__':
    app.run()
