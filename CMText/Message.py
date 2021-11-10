from CMText.MessageBodyTypes import MessageBodyTypes
from CMText.Channels import implementedchannels
from CMText.version import __version__


class Message:
    # Class variables are shared among all instances.
    #minimumNumberOfMessageParts = 1
    #maximumNumberOfMessageParts = 8
    #hybridAppKey = ''
    SENDER_FALLBACK = 'cm.com'
    MESSAGEPARTS_MINIMUM = 1
    MESSAGEPARTS_MAXIMUM = 8
    RECIPIENTS_MAXIMUM = 1000

    def __init__(self, body, **kwargs):
        self.body = body
        self.type = kwargs.get('type', MessageBodyTypes.AUTO)
        self.from_ = kwargs.get('from', self.SENDER_FALLBACK)
        self.to = kwargs.get('to', [])
        self.reference = kwargs.get('reference')
        self.allowedChannels = kwargs.get('allowedChannels', ['SMS'])
        self.richContent = kwargs.get('media')
        self.template = kwargs.get('template')
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
        if len(self.to) + len(recipients) > self.RECIPIENTS_MAXIMUM:
            # TODO: log instead of print
            print('Maximum amount of Recipients exceeded. (' + str(self.RECIPIENTS_MAXIMUM) + ')')
        else:
            self.to = self.to + recipients
