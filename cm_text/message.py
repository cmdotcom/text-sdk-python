from cm_text.message_body_types import MessageBodyTypes
from cm_text.channels import implementedchannels
from cm_text.version import __version__


class Message:
    """
    General purpose Message Class.
    """
    sender_fallback = 'cm.com'
    message_parts_minimum = 1
    message_parts_maximum = 8
    recipients_maximum = 1000

    def __init__(self, body='', **kwargs):
        self.body = body
        self.type = kwargs.get('type', MessageBodyTypes.AUTO)
        # 'from' is a Python keyword, used in imports, therefore using 'from_'
        self.from_ = kwargs.get('from_', self.sender_fallback)
        self.to = kwargs.get('to', [])
        self.reference = kwargs.get('reference')
        self.allowedChannels = kwargs.get('allowedChannels')
        self.richContent = kwargs.get('media')
        self.template = kwargs.get('template')
        self.interactive = kwargs.get('interactive')
        self.customgrouping3 = 'text-sdk-python-' + __version__

        # check if given channels are all valid
        for channel in self.allowedChannels:
            if channel not in implementedchannels:
                # TODO: log instead of print
                print(channel + ' is not a valid Channel name. Check Spelling?')

    def AddRecipients(self, recipients=None):
        """
        Adds an array of extra recipients
        :param recipients: array of recipients
        :return: None
        """
        if recipients is None:
            recipients = []
        # check if total recipients exceeds RECIPIENTS_MAXIMUM
        if len(self.to) + len(recipients) > self.recipients_maximum:
            # TODO: log instead of print
            print('Maximum amount of Recipients exceeded. (' + str(self.recipients_maximum) + ')')
        else:
            self.to = self.to + recipients
