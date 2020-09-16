from CMText.TextClient import TextClient

# Message to be send
message = 'Examples message to be send'

# Recipients
to = ['003156789000', '002134567890']

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

# Send a single message
client.SendSingleMessage(message=message, from_='CM.com', to=to)
