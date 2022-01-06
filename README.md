## 특허 데이터(엑셀) 읽고 데이터베이스에 저장하기
---
### 엑셀 파일
* 엑셀 파일은 최대 5000건까지 저장되어 있음
* 1~7번 row는 데이터가 아닌 특허 검색 관련 정보가 기재되어 있음

### MongoDB
1. 필드 관련
   * 검색 고려하여 인덱싱이 필요한 필드 : title, applicant, claim, abstract
   * 통계로 활용될 수 있는 필드 : ipc, cpc, legal_status, application_date
   * 인덱싱 필요 없이 exact 검색 필드 : application_number, application_date, applicant, legal_status, patent_number, patent_date
2. 인덱싱 없는 것과 있는 것 차이 테스트

### Mongodb 데이터 검색
1. API 개발(Query) 필요

### Git 브랜치
* dev - 기능 단위 푸쉬후 main 으로 PR
* main - PR된 커밋들의 테스트 결과 확인 후 confirm merge

### Test
* unittest