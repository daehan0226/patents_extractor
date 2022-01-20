from os import path
from os.path import dirname, abspath
import sys
from time import time

import asyncio

from config.config import config
from src.modules.logger import Logger
from src.modules.data_file import DataFile
from src.modules.patent_file import get_patents_from_files
from src.modules.patent_documnet import PatentModel

def main(logging, env):
    try:
        main_start_time = time()
        logging.info("===start extracting patents===")

        set_files_path_start_time = time()
        data_dir = path.join((dirname(abspath(__file__))), config["data_dir"][env])
        data_file = DataFile(data_dir)
        logging.info(f"===file count : {len(data_file.full_path_filenames)}===")
        logging.debug(f"===set ful path fienames time : {time()-set_files_path_start_time}")
        
        set_patent_start_time = time()
        patents = get_patents_from_files(logging, data_file.full_path_filenames)
        logging.info(f"===patent count : {len(patents)}===")
        logging.debug(f"===set patents time : {time()-set_patent_start_time}")

        save_in_db_start_time = time()
        asyncio.get_event_loop().run_until_complete(PatentModel.async_insert_patents(patents))
        logging.debug(f"===save in db time : {time()-save_in_db_start_time}")
    
    except KeyError as e:
        logging.error(f"Key error - Check key {e}")
    except Exception as e:
        logging.error(e)
    else:
        logging.debug(f"===total time : {time()-main_start_time}")


if __name__ == "__main__":
    try:
        logging = Logger('extract patents')
        try:
            main(logging, sys.argv[1])
        except:
            raise Exception("Provide dev or server after python ./app.py")
    except Exception as e:
        logging.error(e)