""" 외교부 국가표준코드를 파싱하여 관리하는 클래스 """

# 라이브러리 추가
import pandas as pd
import openpyxl


class CountryCodeHelper:
    def __init__(self, path: str):
        """
        국가표준 코드 csv 파일의 경로를 받아서 관리하는 코드
        :param path: 외교부 국가표준코드 파일 경로
        """

        self._path = path
        self._df = pd.read_csv(self._path, encoding='utf-8', keep_default_na=False)

        # continent 대륙 -> count
        # country 국가 -> cnt
        self._country_codes = {
            value[0]: {'cont_eng': value[3], 'cont_kor': value[4], 'cnt_eng': value[5], 'cnt_kor': value[6]} for value
            in self._df.values}

    def get_cnt_codes(self):
        """
        국가 코드를 리스트로 반환합니다.
        :return list: 국가코드 리스트 반환
        """
        return list(self._country_codes.keys())

    def get_cnt_datas(self):
        """ 파싱된 국가코드를 딕셔너리로 반환합니다. """
        return self._country_codes
