from os import path
from os.path import dirname, abspath
import pandas as pd
import asyncio

from motor import motor_asyncio

from src.modules.patent_documnet import PatentModel
from src.modules.logger import Logger
from config.config import config

from src.utils.helper import get_files_from_dir

def extract_patents_from_excel():

    logging = Logger('extract patents')
    logging.info("start extract patents")
    data_path = path.join(dirname(dirname(abspath(__file__))), config["data_dir"])
    filenames = get_files_from_dir(data_path)

    # PatentModel.get_collection().drop()
    # PatentModel.get_all()
    # return
    # filenames = []
    

    patents = []
    for file in filenames:
        file_path = f"{data_path}/{file}"
        df = pd.read_excel(file_path, skiprows=7).fillna('')
        columns = list(df.columns)
        for i, row in df.iterrows():
            patent = {}
            for col in columns:
                patent[col] = row[col]
            patent_with_en_keys = PatentModel.convert_patent_info_keys_to_english(patent)
            patents.append(PatentModel.set_patent_data(patent_with_en_keys))
        logging.info("finished")
        
    asyncio.get_event_loop().run_until_complete(PatentModel.insert_patents(patents))
