import unittest
import os
import shutil
from os.path import isfile
from datetime import datetime
from src.utils.helper import convert_to_datetime, get_files_from_dir
from src.utils.error import StringDateFormat

class DatetimeHandlerTests(unittest.TestCase): 

    def test_convert_to_datetime(self):
        self.assertEqual(convert_to_datetime("2022.01.05"), datetime(year=2022, month=1, day=5))
        
    def test_convert_to_datetime_raise_error_with_wrong_date_format(self):
        with self.assertRaises(StringDateFormat):
            convert_to_datetime("01.05.2022")

class FileHandlerTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        cls.dir = "test_dir"
        cls.files = ["test1.txt","test2.txt","test3.txt"]

    def setUp(self):
        os.mkdir(self.dir)
        for file in self.files:
            with open(f"{self.dir}/{file}", 'w') as _:
                pass

    def test_get_files_from_dir(self):
        self.assertEqual(get_files_from_dir(self.dir), self.files)
        
    def tearDown(self):
        shutil.rmtree(self.dir)

if __name__ == '__main__':  
    unittest.main()