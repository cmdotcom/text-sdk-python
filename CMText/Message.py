from CMText.MessageBodyTypes import MessageBodyTypes

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
    allowedChannels = []
    richContent = None
    SENDER_FALLBACK = 'cm.com'
    MESSAGEPARTS_MINIMUM = 1
    MESSAGEPARTS_MAXIMUM = 8
    RECIPIENTS_MAXIMUM  = 1000

    #init function of class Message
    def __init__(self, body='', type=MessageBodyTypes.AUTO, from_=None, to=[], reference=None):
        self.body = body
        self.type = type
        if(from_ != None):
            self.from_ = from_
        else:
            self.SENDER_FALLBACK
        self.reference = reference
        self.AddRecipients(recipients=to)

        self.minimumNumberOfMessageParts = self.MESSAGEPARTS_MINIMUM
        self.maximumNumberOfMessageParts = self.MESSAGEPARTS_MAXIMUM

        self.customgrouping3 = 'text-sdk-python-' + '1.0' #+ TextClient.VERSION #find version Texclient


    #add an array of recipients
    def AddRecipients(self, recipients=[]):
        #check if total recipients exceeds RECIPIENTS_MAXIMUM
        if( (len(self.to) + len(recipients)) > self.RECIPIENTS_MAXIMUM):
            print('Maximum amount of Recipients exceeded. (' + str(self.RECIPIENTS_MAXIMUM) + ')')
        else:
            self.to = self.to + [recipients]
