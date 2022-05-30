from CMText.Gateways import Gateways
from CMText.Message import Message
from CMText.WhatsappTemplate import WhatsappTemplate
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
    def SendSingleMessage(self, message, from_, to=[], reference=None, allowedChannels=['SMS']):
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))
        response = self.send()
        return response

    # Add a message to the list
    def AddMessage(self, message, from_='', to=[], reference=None, allowedChannels=['SMS']):
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    # Add a rich message to the list
    def AddRichMessage(self, message, media, from_='', to=[], reference=None, allowedChannels=['Whatsapp']):
        self.messages.append(
            Message(message, media=media, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    # Add a Whatsapp Template message to the list
    def AddWhatsappTemplateMessage(self, template, from_='', to=[], reference=None, media=None):
        self.messages.append(Message(media=media,
                                     from_=from_,
                                     to=to,
                                     reference=reference,
                                     allowedChannels=['Whatsapp'],
                                     template=template))

    # Add an Interactive Whatsapp message to the list
    def add_whatsapp_interactive_message(self, interactive, body='', from_='', to=[], reference=None):
        self.messages.append(
            Message(to=to, body=body, from_=from_, reference=reference, allowedChannels=['Whatsapp'], interactive=interactive))

    def _validate_messages(self, messages, maximum):

        if len(messages) == 0:
            print('No messages in the queue')
            return False
        if len(messages) > maximum:
            print('Messages exceeds MESSAGES_MAXIMUM')
            return False
        return True

    # Send all messages in the list
    def send(self):

        if self._validate_messages(self.messages, self.MESSAGES_MAXIMUM):

            # Set data for post
            data = self.encodeData(self.messages)

            # Set headers for post
            headers = {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": str(len(data)),
                'X-CM-SDK': 'text-sdk-python-' + self.VERSION
            }

            # Send the message(s)
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
        data = {"messages": {"authentication": {"producttoken": self.apikey}}}
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

            # If message is template
            if message.template is not None:
                temp["richContent"] = {
                    "conversation": [{
                        "template":
                            {
                                "whatsapp":
                                    {
                                        "namespace": message.template.namespace,
                                        "element_name": message.template.element_name,
                                        "language":
                                            {
                                                "policy": message.template.language_policy,
                                                "code": message.template.language_code
                                            },
                                        "components": message.template.components
                                    }
                            }
                    }]
                }

            # If message is rich and no template
            if message.template is None and message.richContent is not None:
                temp["richContent"] = {
                    "conversation": [{
                        "text": message.body
                    },
                        {
                            "media": message.richContent,
                        }]
                }

            if message.interactive is not None:
                header = message.interactive.header.encode()
                action = message.interactive.action.encode()

                temp["richContent"] = {
                    "conversation": [{
                        "interactive": {
                            "type": message.interactive.type,
                            "header": header,
                            "body": {
                                "text": message.interactive.body.text
                            },
                            "footer": {
                                "text": message.interactive.footer.text
                            },
                            "action": action
                        }
                    }]
                }

            data['messages']['msg'] = data['messages']['msg'] + [temp]

        # Json encode the data
        data = json.dumps(data)
        return data
