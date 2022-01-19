from datetime import datetime
from src.modules.base_document import BaseDocument
from src.modules.database import Database

from src.utils.helper import convert_to_datetime


class PatentModel(BaseDocument):
    db = Database().get_db()
    meta = {
        "collection": "patent",
        "schema": {
            "title": str,
            "abstract": str,
            "claim": str,
            "applicant": str,
            "application_number": str,
            "application_date": datetime,
            "patent_number": str,
            "patent_date": datetime,
            "ipc_original": str,
            "cpc_original": str,
            "legal_status": str,
            "country": str,
            "ipc": list,
            "cpc": list
        }
    }

    @staticmethod
    def set_patent_data(data):
        
        return {
            **data,
            "ipc" : PatentModel._split_classification(data["ipc_original"]),
            "cpc" : PatentModel._split_classification(data["cpc_original"]),
            "application_date": convert_to_datetime(data["application_date"]),
            "patent_date": convert_to_datetime(data["patent_date"]),
        }
    
    
    @staticmethod
    def _split_classification(data):
        return data.split("|")
    
    @staticmethod
    def convert_patent_info_keys_to_english(data):
        result = {}
        patent_keyes_en = {
            "발명의명칭": "title",
            "요약": "abstract",
            "청구항": "claim",
            "출원인": "applicant",
            "출원번호": "application_number",
            "출원일자": "application_date",
            "등록번호": "patent_number",
            "등록일자": "patent_date",
            "IPC분류": "ipc_original",
            "CPC분류": "cpc_original",
            "법적상태": "legal_status",
            "국가": "country",
        }
        for k, v in data.items():
            if patent_keyes_en.get(k) is not None:
                result[patent_keyes_en[k]] = v
        return result
