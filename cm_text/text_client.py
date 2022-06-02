import json
import requests

from cm_text.gateways import Gateways
from cm_text.message import Message
from cm_text.version import __version__


class TextClient:
    """
    General purpose Text Client for interacting with the CM API
    """
    gateway = ''
    apikey = ''
    messages = []
    MESSAGES_MAXIMUM = 100
    VERSION = __version__

    def __init__(self, apikey, gateway=Gateways.Global):
        self.apikey = apikey
        self.gateway = gateway

    def SendSingleMessage(self, message, from_, to=[], reference=None, allowedChannels=['SMS']):
        """
        Method that sends a single message.

        :param str message: The Message to be send
        :param str from_: Sender
        :param list to: List of strings containing all recipient phone numbers
        :param str reference: The message reference which can be provided by the customer in the outbound message
        :param list allowedChannels: list of strings containing allowed channels to be used.
        """
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))
        response = self.send()
        return response

    def AddMessage(self, message, from_='', to=[], reference=None, allowedChannels=['SMS']):
        """
        Method that appends a default message to the list of messages.

        :param str message: The Message to be send
        :param str from_: Sender
        :param list to: List of strings containing all recipient phone numbers
        :param str reference: The message reference which can be provided by the customer in the outbound message
        :param list allowedChannels: list of strings containing allowed channels to be used.
        """
        self.messages.append(Message(message, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    def AddRichMessage(self, message, media, from_='', to=[], reference=None, allowedChannels=['Whatsapp']):
        """
        Method that appends a rich content message to the list of messages.

        :param str message: The Message to be send
        :param dict media: Dictionary Containing mediaName, mediaUri, mimeType
        :param str from_: Sender
        :param list to: List of strings containing all recipient phone numbers
        :param str reference: The message reference which can be provided by the customer in the outbound message
        :param list allowedChannels: list of strings containing allowed channels to be used.
        """
        self.messages.append(
            Message(message, media=media, from_=from_, to=to, reference=reference, allowedChannels=allowedChannels))

    def AddWhatsappTemplateMessage(self, template, from_='', to=[], reference=None, media=None):
        """
        Method that appends a whatsapp template message to the list of messages.

        :param WhatsappTemplate template: WhatsappTemplate class
        :param str from_: Sender
        :param list to: List of strings containing all recipient phone numbers
        :param str reference: The message reference which can be provided by the customer in the outbound message
        :param dict media: Dictionary Containing mediaName, mediaUri, mimeType
        """
        self.messages.append(
            Message(media=media, from_=from_, to=to, reference=reference, allowedChannels=['Whatsapp'], template=template))

    def add_whatsapp_interactive_message(self, interactive, body='', from_='', to=[], reference=None):
        """
        Method that appends an interactive whatsapp message to the list of messages.

        :param InteractiveMessage interactive: InteractiveMessage class
        :param str body: Fallback text
        :param str from_: Sender
        :param list to: List of strings containing all recipient phone numbers
        :param str reference: The message reference which can be provided by the customer in the outbound message
        """
        self.messages.append(
            Message(to=to, body=body, from_=from_, reference=reference, allowedChannels=['Whatsapp'], interactive=interactive))

    def _validate_messages(self, messages, maximum):
        """
        Method that validates amount of messages.
        """
        if len(messages) == 0:
            print('No messages in the queue')
            return False
        if len(messages) > maximum:
            print('Messages exceeds MESSAGES_MAXIMUM')
            return False
        return True

    def send(self):
        """
        Method that validates message count, constructs post request to be send to (selected) gateway.
        """
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
                response = requests.post(url=self.gateway, data=data, headers=headers)
            except Exception as e:
                print(e)
                raise

            # Clear messages
            self.messages = []

            # Return response
            return response

    def encodeData(self, messages):
        """
        Method that encodes all messages to (gateway) json object to be send as data in post request.
        """
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

            # If reference is set, add it to temp.
            if message.reference is not None:
                temp["reference"] = message.reference

            # If customgrouping3 is set, add it to temp.
            if message.customgrouping3 is not None:
                temp["customGrouping3"] = message.customgrouping3

            # If message is template, set richContent key in temp
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

            # If message is rich and no template, set richContent key in temp
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
