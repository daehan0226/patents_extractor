from datetime import datetime
from src.utils.error import StringDateFormat

def convert_to_datetime(date):
    for format in ["%Y.%m.%d"]:
        try:
            return datetime.strptime(date, format)
        except ValueError as e:
            pass
            
    raise StringDateFormat()