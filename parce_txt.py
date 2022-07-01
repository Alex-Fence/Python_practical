# -*- coding: utf-8 -*-

import os
import pandas as pd


# преобразует строку файла в словарь параметров и значений
def dict_create(source_str: str) -> dict:
    values_dict = dict()
    bitted_str_list = source_str.split(',')
    for values in bitted_str_list:
        if '=' in values:
            temp_lst = values.split('=')
            # так как UV параметр последний, он содержит символ конца строки, убираем его
            if temp_lst[0] == 'UV':
                values_dict[temp_lst[0]] = temp_lst[1][:-1]
            else:
                values_dict[temp_lst[0]] = temp_lst[1]
    return values_dict


source_path = os.path.realpath('C:/Users/ita/Desktop/2.txt')
temp_line = ""
full_dict = dict()

with open(source_path, 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        if len(temp_line) > 0:
            temp_line += line
            # Здесь закоментировано создание чистого файла данных
            # with open("C:\\Users\\ita\\Desktop\\2_.TXT", 'a') as dest_file:
            #     dest_file.write(temp_line)
            temp_dict = dict_create(temp_line)
            # создание словаря "параметр - список значений" для записи в excel файл
            for index, val in temp_dict.items():
                if len(full_dict) == 0 or not (index in full_dict.keys()):
                    full_dict[index] = list()
                full_dict[index].append(val)
            temp_line = ''
        # на параметре Pa идет обрыв строки, убираем его и на следующем витке цикла дописываем остаток строки
        if line.endswith(f'Pa\n'):
            temp_line = line[:-1]
# печать полученного словаря
for key, val in full_dict.items():
    print(f'{key}: {val}')

# запись в файл xlsx
date_frm = pd.DataFrame(full_dict)
date_frm.to_excel('res2.xlsx')
