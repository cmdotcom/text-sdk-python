from CMText.TextClient import TextClient

# Message to be send
message = 'Example message to be sent'
message2 = 'Example 2 message to be sent'

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
