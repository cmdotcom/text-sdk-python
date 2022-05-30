class MessageHeader:
    type = None
    text = None
    media = None

    def __init__(self, type='', text=None):
        self.type = type
        self.text = text


    def encode(self):
        if self.media is not None:
            return self.encode_with_media()

        return self.encode_without_media()

    def encode_without_media(self):
        return {
            "type": self.type,
            "text": self.text
        }

    def encode_with_media(self):
        return {
            "type": self.type,
            "Media": self.media.encode()
        }


class MessageHeaderMedia:
    name = '',
    uri = '',
    mimeType = ""

    def __init__(self, name='', uri='', mime_type=""):
        self.name = name,
        self.uri = uri,
        self.mimeType = mime_type

    def encode(self):
        return {
            "mediaName": ''.join(self.name),
            "mediaUri": ''.join(self.uri),
            "mimeType": self.mimeType
        }
