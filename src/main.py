from os import path
import pandas as pd

from src.modules.patent_documnet import PatentModel
from src.modules.logger import Logger
from config.config import config

from src.utils.helper import get_files_from_dir


def extract_patents_from_excel():
    
    logging = Logger('extract patents')
    logging.info("start extract patents")

    data_path = path.join(path.dirname(__file__), config["data_dir"])
    filenames = get_files_from_dir(data_path)

    for file in filenames:
        df = pd.read_excel(f"{data_path}/{file}", skiprows=7)
        columns = list(df.columns)
        patents = []
        for i, row in df.iterrows():
            patent = {}
            for col in columns:
                patent[col] = row[col]
            patents.append(PatentModel.convert_patent_info_keys_to_english(patent))
            result = PatentModel.create(patent)
            print("result : ", result)
        logging.info(f"patent count : {len(patents)} from {file}" )
        logging.info("finished")
    