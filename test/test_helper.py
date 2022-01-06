import os
import shutil
from datetime import datetime
import pytest
from src.utils.helper import convert_to_datetime, get_files_from_dir
from src.utils.error import StringDateFormat

def test_convert_to_datetime():
    assert(convert_to_datetime("2022.01.05") == datetime(year=2022, month=1, day=5))
    
def test_convert_to_datetime_raise_error():
    with pytest.raises(StringDateFormat):
        convert_to_datetime("01.05.2022")

def test_get_files_from_dr():
    dir = "test_dir"
    files = ["test1.txt","test2.txt","test3.txt"]
    
    os.mkdir(dir)
    for file in files:
        with open(f"{dir}/{file}", 'w') as _:
            pass
        
    assert(set(get_files_from_dir(dir)) == set(files))

    shutil.rmtree(dir)