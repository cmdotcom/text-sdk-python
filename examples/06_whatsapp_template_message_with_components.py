import os
from cm_text import TextClient
from cm_text import WhatsappTemplate

# fetch the API key from environment variables
UNIQUE_API_KEY = os.getenv("CM_API_KEY")
if UNIQUE_API_KEY is None:
    print('Please fill an environment variable named CM_API_KEY with your API key.')

# Recipients
to = ['00123456789', '00986837265']

# Template
template_namespace = "Your_Template_Namespace"
template_element_name = "Your_Template_Name"
template_parameters = [{
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "Name"
                },
                {
                    "type": "text",
                    "text": "test"
                },
                {
                    "type": "text",
                    "text": "Order2"
                },
                {
                    "type": "text",
                    "text": "cm.com"
                }
            ]
        }]

template = WhatsappTemplate(template_namespace, template_element_name, template_parameters)

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

# Add message to queue
client.AddWhatsappTemplateMessage(from_='pythonSDK', to=to, template=template)

# Send message
response = client.send()

# Response is an object of type: https://www.w3schools.com/python/ref_requests_response.asp
print(response.text)
