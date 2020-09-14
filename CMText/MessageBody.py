from CMText.MessageBodyTypes import MessageBodyTypes

class MessageBody:
    content = ''
    type = MessageBodyTypes.AUTO

    def __init__(self, content):
        self.content = content
