""" 리스트를 받아서 csv로 저장 """

import openpyxl
import csv
from tqdm import tqdm


def write_csv(items, file_name):
    """
    이터레이터와 파일의경로를 받아서 csv 파일로 저장한다
    pandas를 쓰지 않는 이유는 메모리 공간을 효율적으로 쓰끼 위해

    :param items: 파일의 데이터가될 이터레이터
    :param file_name: 파일 주소를 포함하는 파일 이름
    """

    header_flag = 0  # 처음 반복에서만 헤더를 추가함

    file = open(file_name, 'a', newline='', encoding='utf-8-sig')

    # 이터레이터를 반복하여 csv 파일을 추가한다
    for item in tqdm(items):
        dict_item = vars(item)
        writer = csv.DictWriter(file, fieldnames=dict_item.keys())

        if header_flag == 0:
            writer.writeheader()
            header_flag += 1

        writer.writerow(dict_item)

    file.close()
