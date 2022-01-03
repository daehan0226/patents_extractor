class Patent:
    def __init__(self, patent_info):
        self.ipc = patent_info["ipc"]
        self.cpc = patent_info["cpc"]
        self.title = patent_info["title"]
        self.abstract = patent_info["abstract"]
        self.application_number = patent_info["application_number"]
        self.applicant = patent_info["applicant"]
        self.application_date = patent_info["application_date"]
        self.claim = patent_info["claim"]
        self.legal_status = patent_info["legal_status"]

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
