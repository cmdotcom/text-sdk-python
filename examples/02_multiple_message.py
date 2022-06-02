import os
from cm_text import TextClient

# fetch the API key from environment variables
UNIQUE_API_KEY = os.getenv("CM_API_KEY")
if UNIQUE_API_KEY is None:
    print('Please fill an environment variable named CM_API_KEY with your API key.')

# Message to be sent
message = 'example message to be sent'
message2 = 'example 2 message to be sent'

# Recipients
to = ['003156789000', '002134567890']

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

# Add a message to the queue
client.AddMessage(message=message, from_='pythonSDK', to=to)
client.AddMessage(message=message2, from_='CM.com', to=to)

# Send the messages
response = client.send()

# Print response
print(response.text)
