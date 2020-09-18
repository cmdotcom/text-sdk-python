from CMText.Gateways import Gateways
from CMText.Message import Message
from CMText.version import __version__
import json
import requests



class TextClient:
    gateway = ''
    apikey = ''
    messages = []
    MESSAGES_MAXIMUM = 100
    VERSION = __version__

    # Initialize Client with defaul Gateway Gateways.Global
    def __init__(self, apikey, gateway=Gateways.Global):
        self.apikey = apikey
        self.gateway = gateway

    # Send 1 message to one or multiple locations
    def SendSingleMessage(self, message, from_, to=[], reference=None, allowedChannels=None):
        self.messages = []
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))
        self.send()

    # Add a message to the list
    def AddMessage(self, message, from_='', to=[], reference=None, allowedChannels=None):
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    # Add a rich message to the list
    def AddRichMessage(self, message, media, from_='', to=[], reference=None, allowedChannels=None):
        self.messages.append(Message(message, media=media, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    # Send all messages in the list
    def send(self):
        if len(self.messages) == 0:
            print('No messages in the queue')
            return
        if len(self.messages) > self.MESSAGES_MAXIMUM:
            print('Messages exceeds MESSAGES_MAXIMUM')
            return

        # Set data for post
        data = self.encodeData(self.messages)

        # Set headers for post
        headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Content-Length": str(len(data)),
             'X-CM-SDK': 'text-sdk-python-' + self.VERSION
         }

        # Send the message
        try:
            response = requests.post("https://gw.cmtelecom.com/v1.0/message", data=data, headers=headers)
        except Exception as e:
            print(e)

        # Clear messages
        self.messages = []
        # Return response
        return response

    # Method to encode Data, Gateway accepts this format
    def encodeData(self, messages):
        # Set productToken
        data = {"messages": {"authentication":{"producttoken": self.apikey}}}
        data['messages']['msg'] = []


        # For each message do this
        for message in messages:
            # List all recipients
            to = []
            for toItem in message.to:
                to = to + [{'number': toItem}]

            # Create message container
            temp = {"allowedChannels": message.allowedChannels,
                    "from": message.from_,
                    "to": to,
                    "body": {
                        "type": message.type,
                        "content": message.body
                    }
                    }

            # If message is rich
            if message.richContent is not None:
                temp["richContent"] = {
                    "conversation": [{
                        "text": message.body
                    },
                    {
                        "media": message.richContent,
                    }]
                }

            data['messages']['msg'] = data['messages']['msg'] + [temp]


        # Json encode the data
        data = json.dumps(data)
        return data
