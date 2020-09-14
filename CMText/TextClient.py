from CMText.Gateways import Gateways
from CMText.Message import Message
from CMText.TextClientRequest import TextClientRequest

class TextClient:
    gateway = ''
    apikey = ''
    messages = []
    MESSAGES_MAXIMUM = 1000
    VERSION = '1.0'

    def __init__(self, apikey, gateway=Gateways.Global):
        self.apikey = apikey
        self.gateway = gateway

    def SendMessage(self, message, from_, to, reference=None):
        try:
            self.messages = Message(message, from_, to, reference)
            return self.send(self)
        except Exception as e:
            print(e)#

    def send(self, messages=[]):
        self.messages = messages or self.messages

        if(len(self.messages) > self.MESSAGES_MAXIMUM):
            print('Messages exceeds MESSAGES_MAXIMUM')

        requestModel = TextClientRequest(self.apikey, self.messages)

        #ch = curl_init($this->gateway); done in php
        #send the message
        try
            print('try')
        except Exception as e:
            print(e)

        



