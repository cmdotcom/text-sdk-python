from CMText.MessageBodyTypes import MessageBodyTypes
from CMText.Channels import Channels
from CMText.version import __version__

class Message:
    body = ''
    type = ''
    customgrouping3 = ''
    from_ = ''
    reference = ''
    to = []
    minimumNumberOfMessageParts = 1
    maximumNumberOfMessageParts = 8
    hybridAppKey = ''
    allowedChannels = ['SMS']
    richContent = None
    SENDER_FALLBACK = 'cm.com'
    MESSAGEPARTS_MINIMUM = 1
    MESSAGEPARTS_MAXIMUM = 8
    RECIPIENTS_MAXIMUM  = 1000

    # init function of class Message
    def __init__(self, body='', type=MessageBodyTypes.AUTO, from_=None, to=[], reference=None, allowedChannels=None, media=None):
        self.body = body
        self.type = type
        if from_ is not None:
            self.from_ = from_
        else:
            self.from_ = self.SENDER_FALLBACK

        # if allowedChannels is set and it exists in Channels:
        ch = Channels()
        if((allowedChannels != None) and ch.Check_Channels(allowedChannels=allowedChannels)):
            self.allowedChannels = allowedChannels

        # if media is not None
        if media is not None:
            self.richContent = media

        self.reference = reference
        self.AddRecipients(recipients=to)

        self.minimumNumberOfMessageParts = self.MESSAGEPARTS_MINIMUM
        self.maximumNumberOfMessageParts = self.MESSAGEPARTS_MAXIMUM

        self.customgrouping3 = 'text-sdk-python-' + __version__

    # add an array of recipients
    def AddRecipients(self, recipients=None):
        if recipients is None:
            recipients = []
        # check if total recipients exceeds RECIPIENTS_MAXIMUM
        if(len(self.to) + len(recipients) > self.RECIPIENTS_MAXIMUM):
            print('Maximum amount of Recipients exceeded. (' + str(self.RECIPIENTS_MAXIMUM) + ')')
        else:
            self.to = self.to + recipients