# 200201 ~
UID = '1loWNF5w3YyMf4UM7Gx3zKwkgNzBMphlqLKcSi7H3PLBf4N%2FwwBqwdyi%2B5XAilxGUiFe2sjIGniphW4lFUtb2w%3D%3D'
ROOT_URL = 'https://apis.data.go.kr/1220000/Itemtrade/'

import xml.etree.ElementTree as ET

import pandas as pd
import requests

import openpyxl

from ExportItem import Item


def save_items_to_csv(items, file_path):
    data = []
    for item in items:
        data.append(item.__dict__)

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')


def read_excel_file(file_path):
    df = pd.read_excel(file_path, header=None, dtype=str)  # header 옵션을 None으로 설정
    data = df.values  # 배열 형태로 데이터 추출
    print(f'{file_path} --- 불러오기 성공')
    #print(data)
    return data


def parse_xml_items(root):
    items = []
    for item_elem in root.findall(".//item"):
        bal_payments = item_elem.find("balPayments").text
        exp_dlr = item_elem.find("expDlr").text
        exp_wgt = item_elem.find("expWgt").text
        hs_code = item_elem.find("hsCode").text
        imp_dlr = item_elem.find("impDlr").text
        imp_wgt = item_elem.find("impWgt").text
        stat_kor = item_elem.find("statKor").text
        year = item_elem.find("year").text

        item = Item(bal_payments, exp_dlr, exp_wgt, hs_code, imp_dlr, imp_wgt, stat_kor, year)
        items.append(item)

    return items


def request_api(api_url):
    response = requests.get(api_url)
    items = []
    if response.status_code == 200:
        # XML 데이터 파싱
        root = ET.fromstring(response.content)

        # XML을 문자열로 변환하여 출력
        xml_string = ET.tostring(root, encoding="utf-8")
        # print(xml_string)

        # <items> 체크
        root_items = root.find('body/items')
        if root_items is None or len(root_items) == 0:
            print("<items> --- 비어있음")
            return items

        items = parse_xml_items(root)
        # 생성된 객체 출력
        # for item in items:
        #     print(item.__dict__)


    else:
        print("API 요청이 실패하였습니다.")

    return items


if __name__ == '__main__':
    # 엑셀 파일 경로
    file_path = "hscode.xlsx"  # 실제 파일 경로로 변경해야 합니다.

    # 엑셀 파일 불러오기
    hscodes = read_excel_file(file_path)

    #print(hscodes)

    items = []
    # 현재 테스트를 위해 최대 한번만 반복함
    # range 부분 수정해야함
    for i in range(1):

        start_year = 200101

        while start_year <= 202201:
            start_year += 100
            end_year = start_year + 11

            strtYymm = str(start_year)
            endYymm = str(end_year)
            hscode = hscodes[i][0]

            print(hscode, hscodes[i][1], start_year, end_year, '--- 데이터 요청 완료')

            api_url = f'getItemtradeList?serviceKey=' \
                      f'{UID}' \
                      f'&strtYymm={strtYymm}' \
                      f'&endYymm={endYymm}' \
                      f'&hsSgn={hscode}'

            request_url = ROOT_URL + api_url
            print(request_url)

            # API 요청 보내기
            items += request_api(request_url)

    # 아이템을 CSV 파일로 저장
    save_items_to_csv(items, "output.csv")