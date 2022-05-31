
class WhatsappTemplate:
    namespace = ''
    element_name = ''
    language_policy = ''
    language_code = ''
    components = []
    media = None

    # init function of class Message
    def __init__(self, namespace, element_name, components=[], media=None, language_policy="deterministic", language_code="en"):
        self.namespace = namespace
        self.element_name = element_name
        self.components = components
        self.media = media
        self.language_policy = language_policy
        self.language_code = language_code
