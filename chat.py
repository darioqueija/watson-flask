import json
import configparser
import os
from flask import Flask, render_template
from flask import request
from flask import jsonify
from ibm_watson import AssistantV2
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

config = configparser.RawConfigParser()
config.read('conf/config.properties')

assistant = None

## WATSON ASSISTANT AUTENTICATION
def watson_assistant():
    global assistant

    api_key = config.get('ibm-cloud', 'ASSISTANT_IAM_APIKEY')
    assistant_url = config.get('environment', 'ASSISTANT_URL')
    version = config.get('environment', 'VERSION')
    without_ssl = bool(config.get('conn-params', 'DISABLE_SSL_VERIFICATION'))

    authenticator = IAMAuthenticator(api_key)
    assistant = AssistantV2(
        version=version,
        authenticator=authenticator
    )

    assistant.set_service_url(assistant_url)
    assistant.set_disable_ssl_verification(without_ssl)

## INTANTIATE FLASK AND WATSON ASSISTANT
app = Flask(__name__, static_url_path='')
watson_assistant()

## LOAD FRONTEND
@app.route('/')
def index():
    return app.send_static_file('index-chat.html')

## CREATE WATSON SESSION ROUTE
@app.route('/api/session')
def session_start():
    try:
        detailed_response = assistant.create_session(
            assistant_id=config.get('environment', 'ASSISTANT_ID')
        )

        return str(detailed_response)
    except ApiException as ex:
        return json.dumps({
          'output': {
            'text': 'Method failed with status code ' + str(ex.code) + ': ' + ex.message
          },
        })

## SEND MESSAGE FROM WATSON ROUTE
@app.route('/api/message', methods=['POST'])
def send_message():
    try:
        json_body = request.get_json(force=True)

        detailed_response = assistant.message(
                assistant_id=config.get('environment', 'ASSISTANT_ID'),
                session_id=json_body['session_id'],
                input={
                    'message_type': 'text',
                    'text': json_body['input']['text']
                }
            )

        return str(detailed_response)
    except ApiException as ex:
        return json.dumps({
          'output': {
            'text': 'Method failed with status code ' + str(ex.code) + ': ' + ex.message
          },
        })

## DESTROY WATSON SESSION ROUTE
@app.route('/api/interrupt', methods=['POST'])
def session_stop():
    try:
        json_body = request.get_json(force=True)

        detailed_response = assistant.delete_session(
                assistant_id=config.get('environment', 'ASSISTANT_ID'),
                session_id=json_body['session_id']
            )

        return str(detailed_response)
    except ApiException as ex:
        return json.dumps({
          'output': {
            'text': 'Method failed with status code ' + str(ex.code) + ': ' + ex.message
          },
        })

@app.route('/api/webhook', methods=['POST'])
def webhook():
    return jsonify({ "name": "João da Silva" })

## CONFIGURE FLASK INITIALIZE
port = int(os.getenv('PORT', 8000))

def main():
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
