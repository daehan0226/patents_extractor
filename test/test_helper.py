import os
import shutil
from datetime import datetime
import pytest
from src.utils.helper import convert_to_datetime
from src.utils.error import StringDateFormat
from src.modules.data_file import DataFile

def test_convert_to_datetime():
    assert(convert_to_datetime("2022.01.05") == datetime(year=2022, month=1, day=5))
    
def test_convert_to_datetime_raise_error():
    with pytest.raises(StringDateFormat):
        convert_to_datetime("01.05.2022")

def test_get_files_from_dir():
    dir = "test_dir"
    files = ["test1.txt","test2.txt","test3.txt"]
    
    os.mkdir(dir)
    for file in files:
        with open(f"{dir}/{file}", 'w') as _:
            pass
        
    assert set(DataFile(dir)._get_files_from_data_dir()) == set(files)

    shutil.rmtree(dir)