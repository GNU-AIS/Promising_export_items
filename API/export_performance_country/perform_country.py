"""
관세청 품목별 국가별 수출입실적 공공데이터 API를 이용하여
품목별 국가별 수출입실적을 조회하여 CSV 파일로 저장합니다.
"""

# 라이브러리 추가
import requests

# 클래스, 모듈 추가
from my_class.ExportItem import ExportItem
from my_module.api_keys import get_uid
from my_module.api_utils import response_xml_parsing, get_request_url


def main():
    request_url = get_request_url(get_uid(), 201601, 201601, "1001999090", "US")
    response = requests.get(request_url)

    items = []
    if response.status_code != 200:
        # 응답 실패
        print(response.status_code)
        print(response.text)

    else:
        # 응답 성공, 문자열로 xml을 파싱함
        items = response_xml_parsing(response.content)

    # items 리스트에 들어 있는 모든 ExportItem 객체의 정보를 출력
    for item in items:
        print(vars(item))


if __name__ == "__main__":
    main()
