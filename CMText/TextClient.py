from CMText.Gateways import Gateways
from CMText.Message import Message

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
        self.messages.append(Message(message, from_, to, reference))
        self.send(self)

    #add a message to the list
    def AddMessage(self, message, from_='', to=[], reference=None):
        self.messages.append(Message(message, from_=from_, to=to, reference=reference))

    #send all messages in the list
    def send(self, messages=None):
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
             'X-CM-SDK': 'text-sdk-python-1.0'
         }

        #send the message
        try:
            print(1)


        except Exception as e:
            print(e)

        #clear messages
        self.messages = []


    def encodeData(self, messages): # hier bezig

        #set productToken
        data = {"messages": {"authentication":{"producttoken": self.apikey}}}

        #for each message do this
        for message in messages:
            to = []
            for toItem in message.to:
                to = {'number': toItem}

            #create message container
            temp = {"allowedChannels": message.allowedChannels,
                    "from": message.from_,
                    "to": to,
                    "body": {
                        "type": message.type,
                        "content": message.body
                    }
                    }


            data['messages']['msg'] = temp
            #print(message)
            print(data['messages'])


        print(messages)

        return data
