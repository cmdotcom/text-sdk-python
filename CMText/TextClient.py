from CMText.Gateways import Gateways
from CMText.Message import Message
import json
import requests

class TextClient:
    gateway = ''
    apikey = ''
    messages = []
    MESSAGES_MAXIMUM = 100
    VERSION = '1.0'

    def __init__(self, apikey, gateway=Gateways.Global):
        self.apikey = apikey
        self.gateway = gateway

    #send 1 message to one or multiple locations
    def SendSingleMessage(self, message, from_, to=[], reference=None):
        self.messages = []
        self.messages.append(Message(message, from_=from_, to=to, reference=reference))
        self.send()

    #add a message to the list
    def AddMessage(self, message, from_='', to=[], reference=None):
        self.messages.append(Message(message, from_=from_, to=to, reference=reference))

    #send all messages in the list
    def send(self):
        if(len(self.messages) == 0):
            print('No messages in the queue')
            return
        if(len(self.messages) > self.MESSAGES_MAXIMUM):
            print('Messages exceeds MESSAGES_MAXIMUM')
            return

        #set data for post
        data = self.encodeData(self.messages)

        #set headers for post
        headers = {
             "Content-Type": "application/json; charset=utf-8",
             "Content-Length": str(len(data)),
             'X-CM-SDK': 'text-sdk-python-' + self.VERSION
         }

        #send the message
        try:
            print(data)
            #html = requests.post("https://gw.cmtelecom.com/v1.0/message", data=data, headers=headers).text
            #print(html)

        except Exception as e:
            print(e)

        #clear messages
        self.messages = []

    #Method to encode Data, Gateway accepts this format
    def encodeData(self, messages):
        #set productToken
        data = {"messages": {"authentication":{"producttoken": self.apikey}}}
        data['messages']['msg'] = []
        #for each message do this
        for message in messages:
            #list all recipients
            to = []
            for toItem in message.to:
                to = to + [{'number': toItem}]

            #create message container
            temp = {"allowedChannels": message.allowedChannels,
                    "from": message.from_,
                    "to": to,
                    "body": {
                        "type": message.type,
                        "content": message.body
                    }
                    }
            data['messages']['msg'] = data['messages']['msg'] + [temp]
        #json encode the data
        data = json.dumps(data)
        return data
