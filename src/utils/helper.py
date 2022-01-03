from os import path, listdir

def get_files_from_dir(data_path):
    return[f for f in listdir(data_path) if path.isfile(path.join(data_path, f))]