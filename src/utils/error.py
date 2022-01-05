class Error(Exception):
    """Base class for other exceptions"""
    pass

class StringDateFormat(Error):
    """Raised when the input value is a new date foramt"""
    pass