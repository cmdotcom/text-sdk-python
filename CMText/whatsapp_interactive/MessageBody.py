class MessageBody:
    text = ''

    def __init__(self, text):
        self.text = text

    def encode(self):
        return self.__dict__
