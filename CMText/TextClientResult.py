

class TextClientResult:

    httpStatusCode = None
    response = ''

    def __init__(self, httpStatusCode, responseBody):
        self.httpStatusCode = httpStatusCode
        self.response = responseBody