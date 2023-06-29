"""
관세청 품목별 국가별 수출입실적 공공데이터 API를 이용하여
품목별 국가별 수출입실적을 조회하여 CSV 파일로 저장합니다.
"""

# 라이브러리 추가
import requests
from datetime import datetime
from tqdm import tqdm

# 클래스, 모듈 추가
from my_class.ExportItem import ExportItem
from my_module.api_keys import get_uid
from my_module.api_utils import response_xml_parsing, get_request_url
from my_module.csv_utils import write_csv
from API.utils.cnt_code.CountryCodeHelper import CountryCodeHelper

def main():

    code_helper = CountryCodeHelper(
        r'C:\Users\ymail\WorkSpaces\codingstudy\pypy\Promising_export_items\API\utils\cnt_code\code.csv')
    cnt_codes = code_helper.get_cnt_codes()  # 외교부 표준 국가 코드를 리스트로 반환

    # 국가코드 리스트에 들어있는 모든 국가를 설정한 변수로 API 요청
    cnt_does_list = ['US']

    # 년도 범위를 정해서 반복
    start_year = 2016
    end_year = 2022

    # 응답 데이터를 저장할 리스트
    items = []

    for country_code in tqdm(cnt_does_list):
        for now_year in range(start_year, end_year + 1):

            # 요청 변수
            start_month = str(now_year) + '01'  # 시작월
            end_month = str(now_year) + '12'  # 종료월
            hs_sgn = ''  # 참고 hs 코드 (없어도 됨)
            cnt_cd = country_code  # 국가 코드

            # 요청 변수를 url 유틸함수를 통해 대입 하여 url을 받고 api 요청
            request_url = get_request_url(get_uid(), start_month, end_month, hs_sgn, cnt_cd)
            response = requests.get(request_url)

            if response.status_code == 200:
                # 응답 성공, 문자열로 xml을 파싱함
                items = response_xml_parsing(response.content)

            else:
                # 응답 실패
                print(response.status_code)
                print(response.text)


    # items 리스트에 들어 있는 모든 ExportItem 객체를 딕셔너리로 변환후 리스트에 저장
    dict_items_list = []

    for item in tqdm(items):
        d = vars(item)
        dict_items_list.append(d)

    # csv 파일 저장을 위한 경로 설정
    file_path = r'C:\Users\ymail\WorkSpaces\codingstudy\pypy\Promising_export_items\API\export_performance_country\result'

    # 파일 이름을 현재 시간으로 설정
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d%H%M%S")
    file_name = file_path + r'\result' + formatted_date + r'.csv'

    # csv 파일 생성
    write_csv(dict_items_list, file_name)


if __name__ == "__main__":
    main()
