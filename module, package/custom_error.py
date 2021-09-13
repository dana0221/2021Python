class InvalidLengthError(Exception):
    def __init__(self, message):
        super(InvalidLengthError, self).__init__()