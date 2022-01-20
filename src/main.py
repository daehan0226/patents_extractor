from os import path
from os.path import dirname, abspath
import asyncio
from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd

from config.config import config
from src.modules.patent_documnet import PatentModel
from src.modules.logger import Logger
from src.utils.helper import get_files_from_dir


data_path = path.join(dirname(dirname(abspath(__file__))), config["test_data_dir"])

def get_patent_info_files(file):
    result = []
    file_path = f"{data_path}/{file}"
    df = pd.read_excel(file_path, skiprows=7).fillna('')
    columns = list(df.columns)
    for _, row in df.iterrows():
        patent = {}
        for col in columns:
            patent[col] = row[col]
        patent_with_en_keys = PatentModel.convert_patent_info_keys_to_english(patent)
        result.append(PatentModel.set_patent_data(patent_with_en_keys))
    return result

def extract_patents_from_excel():
    logging = Logger('extract patents')
    logging.info("start extract patents")
    filenames = get_files_from_dir(data_path)
    patents = []
    with ProcessPoolExecutor(max_workers=5) as executor:
        future_to_file = {executor.submit(get_patent_info_files, filename): filename for filename in filenames}
        
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            logging.debug(f"getting patent from {file}")
            try:
                data = future.result()
                patents.extend(data)
            except Exception as exc:
                logging.error(f"{file} generated an exception: {exc}")
            else:
                logging.info(f'{file} page is {len(data)} bytes')
    
    logging.info(f"save patents in mongodb {len(patents)}")
    asyncio.get_event_loop().run_until_complete(PatentModel.async_insert_patents(patents))
