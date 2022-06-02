from cm_text.whatsapp_interactive.interactive_message import InteractiveMessage
from cm_text.whatsapp_interactive.message_action import MessageAction, MessageActionSection, MessageActionRow, \
    MessageActionButton, MessageActionButtonReply
from cm_text.whatsapp_interactive.message_body import MessageBody
from cm_text.whatsapp_interactive.message_header import MessageHeader, MessageHeaderMedia
from cm_text.whatsapp_interactive.message_footer import MessageFooter


class MessageBuilder:
    interactiveMessage = None

    @staticmethod
    def create_interactive_message(type, header=None, body=None, footer=None, action=None):
        return InteractiveMessage(type=type, header=header, body=body, footer=footer, action=action)

    @staticmethod
    def create_interactive_message_action(button='', buttons=[], sections=[]):
        return MessageAction(button=button, buttons=buttons, sections=sections)

    @staticmethod
    def create_interactive_message_action_row(title='', id='', description=''):
        return MessageActionRow(id=id, title=title, description=description)

    @staticmethod
    def create_interactive_message_action_section(title='', rows=[]):
        if rows is None:
            raise Exception("Row cannot be empty")

        section = MessageActionSection(title)

        print(section)
        [section.add_row(row) for row in rows]
        return section

    @staticmethod
    def create_interactive_message_action_button(type='', reply=MessageActionButtonReply):
        if reply is None:
            raise Exception("Reply button is required")

        button = MessageActionButton(type=type, reply=reply)
        return button

    @staticmethod
    def create_interactive_message_action_button_reply(id='', title=''):
        return MessageActionButtonReply(id=id, title=title)

    @staticmethod
    def create_interactive_message_body(text=''):
        return MessageBody(text=text)

    @staticmethod
    def create_interactive_message_footer(text=''):
        return MessageFooter(text)

    @staticmethod
    def create_interactive_message_header(type='', text='', media=MessageHeaderMedia):
        header = MessageHeader(type=type, text=text)
        if media is not None:
            header.media = media

        return header

    @staticmethod
    def create_interactive_message_header_media(name='', uri='', mimeType=''):
        return MessageHeaderMedia(name, uri, mimeType)
