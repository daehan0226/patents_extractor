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
        df = pd.read_excel(f"{data_path}/{file}", skiprows=7).fillna('')
        columns = list(df.columns)
        for i, row in df.iterrows():
            patent = {}
            for col in columns:
                patent[col] = row[col]
            patent_with_en_keys = PatentModel.convert_patent_info_keys_to_english(patent)
            patent = PatentModel.set_patent_data(patent_with_en_keys)
            print(patent)
            # result = PatentModel.create(**patent)
            # print("result : ", result)
        logging.info("finished")
    