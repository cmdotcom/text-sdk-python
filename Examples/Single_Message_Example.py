import os
from CMText.TextClient import TextClient

# fetch the API key from environment variables
UNIQUE_API_KEY = os.getenv("CM_API_KEY")
if UNIQUE_API_KEY is None:
    print('Please fill an environment variable named CM_API_KEY with your API key.')

# Message to be sent
message = 'Examples message to be sent'

# Recipients
to = ['003156789000', '002134567890']

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

# Send a single message
client.SendSingleMessage(message=message, from_='CM.com', to=to)
