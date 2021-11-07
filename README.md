# Instalation

* Install [anaconda](https://docs.anaconda.com/anaconda/install/index.html).
* Create [conda env](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
* Install project dependencies:

~~~
pip install -r requirements.txt
~~~

# Configuration

## Watson Assistant

* Create your [Watson Assistant on IBM Cloud](https://cloud.ibm.com/catalog/services/watson-assistant):
	* [Getting started](https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started).
* Create configuration file:

~~~
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
