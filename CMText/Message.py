from CMText.MessageBody import MessageBody
from CMText.TextClient import TextClient

class Message:
    body = ''
    customgrouping3 = ''
    from_ = ''
    reference = ''
    to = ['1', '2']
    minimumNumberOfMessageParts = 1
    maximumNumberOfMessageParts = 8
    hybridAppKey = ''
    allowedChannels = []
    richContent = None
    SENDER_FALLBACK = 'cm.com'
    MESSAGEPARTS_MINIMUM = 1
    MESSAGEPARTS_MAXIMUM = 8
    RECIPIENTS_MAXIMUM  = 1000

    #init function of class Message
    def __init__(self, body='', from_=None, to=[], reference=None):
        self.body = MessageBody(body)
        self.from_ = from_ or self.SENDER_FALLBACK
        self.reference = reference
        self.AddRecipients(self, to)

        self.minimumNumberOfMessageParts = self.MESSAGEPARTS_MINIMUM
        self.maximumNumberOfMessageParts = self.MESSAGEPARTS_MAXIMUM

        self.customgrouping3 = 'text-sdk-python-' + TextClient.VERSION


    #add an array of recipients
    def AddRecipients(self, recipients):
        #check if total recipients exceeds RECIPIENTS_MAXIMUM
        if( (len(self.to) + len(recipients)) > self.RECIPIENTS_MAXIMUM):
            print('Maximum amount of Recipients exceeded. (' + self.RECIPIENTS_MAXIMUM + ')')
        else:
            self.to = self.to + recipients
