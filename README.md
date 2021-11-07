# Instalation

* Install [anaconda](https://docs.anaconda.com/anaconda/install/index.html).
* Create [conda env](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
* Install [pip](https://docs.python.org/3/installing/index.html).
* Install project dependencies:

~~~ bash
pip install -r requirements.txt
~~~

# Configuration

## Watson Assistant

* Create your [Watson Assistant on IBM Cloud](https://cloud.ibm.com/catalog/services/watson-assistant):
	* [Getting started](https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started).
* Create configuration file:

~~~ bash
cp conf/config.properties.template conf/config.properties
~~~

* Configure keys and urls
	* Go to [resources list](https://cloud.ibm.com/resources) > Services and Software > Watson Assitant Dallas:
		* ASSISTANT_IAM_APIKEY
		* ASSISTANT_URL
	* Go to [Watson Assistant](https://us-south.assistant.watson.cloud.ibm.com/instances) > Assistants > Choose Assistant > Settings:
		* ASSISTANT_ID
		* ASSISTANT_IAM_URL
	* Read about [versioning](https://github.com/watson-developer-cloud/api-guidelines/#versioning) and configure:
		* VERSION

## Flask App

* Configure environment variables from Flask:

~~~ bash
export FLASK_ENV=development
export FLASK_APP=<app-name>
~~~

Choose app

This project has two apps:
1. hello
1. chat

### Hello

~~~ bash
export FLASK_APP=hello
~~~

Endpoints:
* / -> hello world with flask
* /start -> create watson session
* /talk/<message> -> send message to watson
* /stop -> destroy watson session

### Chat

~~~ bash
export FLASK_APP=chat
~~~

This app fork a IBM frontend code from [assistant-simple](https://github.com/watson-developer-cloud/assistant-simple) to provide a web chat. This is interact from flask web services and watson assistant.

# Run App

After config app, run flask:

~~~ bash
flask run
~~~

Access your browser __http://localhost:5000/__.