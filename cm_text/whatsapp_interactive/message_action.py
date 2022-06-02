class MessageActionRow:
    """Source: https://developers.facebook.com/docs/whatsapp/guides/interactive-messages
    Title of the row.
    Maximum length of 24 characters
    """
    title = ''

    """
    Id of the row
    Maximum length of 200 characters
    """
    id = ''

    """
    Description of the row
    Maximum length of 72 characters
    """
    description = ''

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def create_new_row(id, title, description):
        row = MessageActionRow(id=id, title=title, description=description)
        return row

    def encode(self):
        return self.__dict__


class MessageActionSection:
    title = ''
    rows = []

    def __init__(self, title):
        self.title = title
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def encode(self):
        return {
            "title": self.title,
            "rows": [z.encode() for z in self.rows]
        }


class MessageActionButton:
    type = ''
    reply = None

    def __init__(self, type, reply):
        self.type = type
        self.reply = reply

    def encode(self):
        return {
            "type": self.type,
            "reply": self.reply.encode()
        }


class MessageActionButtonReply:
    id = ''
    title = ''

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def encode(self):
        return self.__dict__


class MessageAction:
    button = ''
    buttons = []
    sections = []

    def __init__(self, button='', buttons=[], sections=[]):
        self.button = button
        self.buttons = buttons
        self.sections = sections

    def add_section(self, section):
        self.sections.append(section)

    def add_button(self, button):
        self.buttons.append(button)

    def encode(self):
        if not self.buttons:
            return {
                "button": ''.join(self.button),
                "sections": [z.encode() for z in self.sections]
            }
        else:
            return {
                "buttons": [x.encode() for x in self.buttons]
            }
