# 라이브러리 import
import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

import pprint
import json
import codecs

# url 입력
countrys = ['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA',
            'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW',
            'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW',
            'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ',
            'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR',
            'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ',
            'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KY', 'KZ', 'LA',
            'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK',
            'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE',
            'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM',
            'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG',
            'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF',
            'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY',
            'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
data = [
    ['국명', '면적', '인구', '언어', '종교']
]

atr = ['natnNm']

atr2 = ['natnNm', 'area',
        'poplCnt',
        'langNm',
        'relgnNm']
for country in countrys:
    try:
        url = f'http://apis.data.go.kr/B410001/natnInfoService/natnInfo?serviceKey=zYvc9sk%2FOTZIY%2FO%2BZ0LBh7Rt0GOdQJooBgJAppJ%2B00dCvI%2F5z7nIDDw%2BL7OIAC9qvnLm84nf1FRCD3808acB2A%3D%3D&type=xml&isoWd2CntCd={country}'

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'xml')
        head = soup.find('response').find('body').find('items').find('item')

        title = []

        # 저장할 데이터

        for a in atr:
            title.append(head.find(a).text)

        data.append(title)
    except:
        continue

# CSV 파일 열기
with open('data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    # CSV 파일 작성을 위한 writer 객체 생성
    csv_writer = csv.writer(file)

    # 데이터를 CSV 파일에 쓰기
    for row in data:
        csv_writer.writerow(row)
