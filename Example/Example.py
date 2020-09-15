from CMText.TextClient import TextClient

#message to be send
message = 'Example message to be send'

#recipients
to = ['123456789000', '001234567890']

#instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

#usecase 1, send a single message
client.SendSingleMessage(message=message, from_='CM.com', to=to)

#usecase 2, queue messages by adding them, Send all of them at once
client.AddMessage(message=message, from_='pythonSDK', to=to)
client.send()