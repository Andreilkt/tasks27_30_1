#https://#stackoverflow.com/questions/22765313/when-import-docx-in-python3-3-i-
# have-error-importerror-no-module-named-excepti

from BaseExceptions import ValueError

class ValidationError(ValueError):
    def __init__(self, message):
        ValueError.__init__(self, message)

class TooSmallValue(ValidationError):
    def __init__(self, min_val, msg):
        ValidationError.__init__(self, msg)
        self.min_val = min_val

class TooBigValue(ValidationError):
    def __init__(self, max_val, msg):
        ValidationError.__init__(self, msg)
        self.max_val = max_val
