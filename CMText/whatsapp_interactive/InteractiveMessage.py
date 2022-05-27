class InteractiveMessage:
    type = ""
    header = None
    body = None
    footer = None
    action = None

    def __init__(self, type, header=None, body=None, footer=None, action=None):
        self.type = type
        self.header = header
        self.body = body
        self.footer = footer
        self.action = action
