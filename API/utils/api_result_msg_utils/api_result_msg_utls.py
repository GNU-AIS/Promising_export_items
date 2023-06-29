""" api header에 result 코드와 메시지를 파싱하는 유틸 모듈 """
from lxml import etree


def print_results(root):
    """ 결과를 파싱하여 반환 """
    result_code = root.findtext('header/resultCode')
    result_msg = root.findtext('header/resultMsg')
    return result_code, result_msg
