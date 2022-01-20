from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd

from src.modules.patent_documnet import PatentModel


def set_patents_from_file(file_path):
    result = []
    df = pd.read_excel(file_path, skiprows=7).fillna('')
    columns = list(df.columns)
    for _, row in df.iterrows():
        patent = {}
        for col in columns:
            patent[col] = row[col]
        patent_with_en_keys = PatentModel.convert_patent_info_keys_to_english(patent)
        result.append(PatentModel.set_patent_data(patent_with_en_keys))
    return result


def get_patents_from_files(logging, file_path_list):
    result = []
    with ProcessPoolExecutor(max_workers=5) as executor:
        future_to_file = {executor.submit(set_patents_from_file, file_path): file_path for file_path in file_path_list}
        
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            logging.debug(f"getting patent from {file}")
            try:
                data = future.result()
                result.extend(data)
            except Exception as exc:
                logging.error(f"{file} generated an exception: {exc}")
            else:
                logging.debug(f'{file} page is {len(data)} bytes')
    return result