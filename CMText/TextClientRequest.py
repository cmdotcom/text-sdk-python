

class TextClientRequest:
    productToken = ''
    messages = []

    def __init__(self, apiKey, messages):
        self.productToken = apiKey
        self.messages = messages

