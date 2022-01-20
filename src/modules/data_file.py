from os import path, listdir

class DataFile:

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.full_path_filenames = self._get_full_path_filenames()

    def _get_files_from_data_dir(self):
        return [f for f in listdir(self.data_dir) if path.isfile(path.join(self.data_dir, f))]

    def _get_full_path_filenames(self):
        filenames = self._get_files_from_data_dir()     
        return [f"{self.data_dir}{file}" for file in filenames]   