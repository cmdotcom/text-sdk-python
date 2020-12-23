#Class chanels
#Contains all known channels
class Channels:

    channels = {'SMS',
                'Whatsapp',
                'Push',
                'RCS',
                'Viber',
                'Voice',
                'iMessage',
                'Line',
                'Twitter',
                'MobilePush',
                }

    def Check_Channels(self, allowedChannels):
        for allowedChannel in allowedChannels:
            if(not allowedChannel in self.channels):
                print(allowedChannel + ' is not a valid Channel name. Check Spelling?')
                return False
        return True