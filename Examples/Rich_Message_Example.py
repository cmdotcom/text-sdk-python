import os
from CMText.TextClient import TextClient

# fetch the API key from environment variables
UNIQUE_API_KEY = os.getenv("CM_API_KEY")
if UNIQUE_API_KEY is None:
    print('Please fill an environment variable named CM_API_KEY with your API key.')

# Message to be sent
message = 'Examples message to be sent'

# Media to be sent
media = {
            "mediaName": "conversational-commerce",
            "mediaUri": "https://www.cm.com/cdn/cm/cm.png",
            "mimeType": "image/png"
        }

# AllowedChannels in this case Whatsapp
allowedChannels = ['Whatsapp']

# Recipients
to = ['003156789000', '002134567890']

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

# Add a Rich message to the queue
client.AddRichMessage(message=message, from_='pythonSDK', to=to, allowedChannels=allowedChannels, media=media)

# Send the messages
response = client.send()

# Print response
print(response.text)
