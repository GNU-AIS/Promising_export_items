""" 리스트를 받아서 csv로 저장 """

import pandas as pd
import openpyxl


def write_csv(items: list, path_name: str):
    """ 리스트와 경로를 받아서 csv 파일로 저장 """

    with open(path_name, 'w', newline='', encoding='utf-8-sig') as file:
        df = pd.DataFrame(items,
                          columns=['year', 'statCdCntnKor1', 'statCd', 'statKor', 'hsCd', 'expWgt', 'expDlr', 'impWgt',
                                   'impDlr', 'balPayments'])

        df.to_csv(file, index=True, encoding='utf-8-sig')
