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
export PORT=${?:8000}
~~~

Default port is 8000.

Choose app

This project has two apps:
1. hello
1. chat

### Hello

Endpoints:
* / -> hello world with flask
* /start -> create watson session
* /talk/<message> -> send message to watson
* /stop -> destroy watson session

### Chat

This app fork a IBM frontend code with name [assistant-simple](https://github.com/watson-developer-cloud/assistant-simple) to provide a web chat. Frontend interacts with flask web services and watson assistant.

# Run App

After config app, run flask:

~~~ bash
python hello.py
~~~

or

~~~ bash
python chat.py
~~~

Access in your browser __http://localhost:8000/__.

# Run on IBM Bluemix

* Create your app python on [IBM Cloud Foundry](https://cloud.ibm.com/cloudfoundry/overview):
	* Create a python application.
	* Add name application: <APP_NAME>.
* Open [Cloud IBM shell](https://cloud.ibm.com/shell).
* Clone this project and configure.

~~~ bash
git clone https://github.com/marcelodcc/watson-flask
~~~

* Configure file config.properties like defined on [configuration session](https://github.com/marcelodcc/watson-flask#configuration).
* Configure property __name__ with <APP_NAME> on __manifest.yml__ file.
* Install project dependencies:

~~~ bash
pip install -r requirements.txt
~~~

* Deploy application:

~~~ bash
ibmcloud cf push <APP_NAME>
~~~

* Get path your application:

~~~ bash
ibmcloud cf apps
~~~

Access in your browser __https://<APP_NAME>.<your_region>.cf.appdomain.cloud__.
