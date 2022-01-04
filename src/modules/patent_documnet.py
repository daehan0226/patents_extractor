from src.modules.base_document import BaseDocument
from src.modules.database import Database


class PatentModel(BaseDocument):
    db = Database().get_db()
    meta = {
        "collection": "patent",
        "schema": {
            "application_number": str,
            "application_date": str,
            "title": str,
            "applicant": str,
            "ipc": str,
            "cpc": str,
            "legal_status": str,
            "abstract": str,
            "claim": str,
        }
    }
    
    @staticmethod
    def convert_patent_info_keys_to_english(data):
        result = {}
        patent_en = {
            "출원번호": "application_number",
            "출원일자": "application_date",
            "발명의명칭": "title",
            "출원인": "applicant",
            "IPC분류": "ipc",
            "CPC분류": "cpc",
            "법적상태": "legal_status",
            "요약": "abstract",
            "청구항": "claim",
        }
        for k, v in data.items():
            if patent_en.get(k) is not None:
                result[patent_en[k]] = v
        return result
