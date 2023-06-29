"""
관세청 품목별 국가별 수출입실적 API 관련 유틸 모듈
"""

# 라이브러리 추가
from lxml import etree

# 클래스 추가
from API.export_performance_country.my_class.ExportItem import ExportItem


def get_root_url():
    """ API 요청 주소 End Point 반환 """
    ROOT_URL = 'https://apis.data.go.kr/1220000/nitemtrade/'
    return ROOT_URL


def response_xml_parsing(content):
    """ 응답받은 content를 파싱하여 ExportItem 클래스 리스트로 반환 """

    items = []
    root = etree.fromstring(content)  # 응답을 바이트 형태로 불러옴

    for item_element in root.xpath('//item'):
        hsCd = item_element.findtext('hsCd')

        # item 중에 hs 코드가 없는 경우 건너뜀
        if hsCd == '-':
            continue

        balPayments = item_element.findtext('balPayments')
        expDlr = item_element.findtext('expDlr')
        expWgt = item_element.findtext('expWgt')
        impDlr = item_element.findtext('impDlr')
        impWgt = item_element.findtext('impWgt')
        statCd = item_element.findtext('statCd')
        statCdCntnKor1 = item_element.findtext('statCdCntnKor1')
        statKor = item_element.findtext('statKor')
        year = item_element.findtext('year')

        # ExportItem 객체 생성하고 리스트에 추가
        items.append(
            ExportItem(
                balPayments,
                expDlr,
                expWgt,
                hsCd,
                impDlr,
                impWgt,
                statCd,
                statCdCntnKor1,
                statKor, year
            ))

    return items


def get_request_url(serviceKey, strtYymm, endYymm, hsSgn, cntyCd):
    """ End Point 경로와 api 요청 변수를 넣어서 URL을 만들고 반환 """

    # API 호출을 위한 요청 변수 URL 생성
    api_url = f'getNitemtradeList?serviceKey={serviceKey}' \
              f'&strtYymm={strtYymm}' \
              f'&endYymm={endYymm}' \
              f'&hsSgn={hsSgn}' \
              f'&cntyCd={cntyCd}'

    return get_root_url() + api_url
