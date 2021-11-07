import json
import configparser
from flask import Flask, render_template
from ibm_watson import AssistantV2
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

config = configparser.RawConfigParser()
config.read('conf/config.properties')

session_id = ''
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
app = Flask(__name__)
watson_assistant()

## LOAD FRONTEND
@app.route('/')
def index():
    return render_template('index.html')

## CREATE WATSON SESSION ROUTE
@app.route('/start')
def start():
    global session_id

    try:
        if not session_id:
            response = assistant.create_session(
                assistant_id=config.get('environment', 'ASSISTANT_ID')
            ).get_result()

            session_id = response['session_id']

            return json.dumps(response, indent=2)
        else:
            return "Session has already started: " + str(session_id)
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

## DESTROY WATSON SESSION ROUTE
@app.route('/stop')
def stop():
    global session_id
    try:
        if session_id:
            response = assistant.delete_session(
                assistant_id=config.get('environment', 'ASSISTANT_ID'),
                session_id=session_id
            ).get_result()

            session_id = ''
            return json.dumps(response, indent=2) 
        else:
            return "Session not started."
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

## SEND MESSAGE FROM WATSON ROUTE
@app.route('/talk/<string:text>')
def talk(text):
    try:
        if session_id:
            response = assistant.message(
                assistant_id=config.get('environment', 'ASSISTANT_ID'),
                session_id=session_id,
                input={
                    'message_type': 'text',
                    'text': text
                }
            ).get_result()

            return json.dumps(response, indent=2)
        else:
            return "Session not started."
    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

## CONFIGURE FLASK INITIALIZE
port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)