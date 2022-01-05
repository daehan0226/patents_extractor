from os import path, listdir
from datetime import datetime

from src.utils.error import StringDateFormat

def get_files_from_dir(data_path):
    return [f for f in listdir(data_path) if path.isfile(path.join(data_path, f))]

def convert_to_datetime(date):
    for format in ["%Y.%m.%d"]:
        try:
            return datetime.strptime(date, format)
        except ValueError as e:
            pass
            
    raise StringDateFormat()