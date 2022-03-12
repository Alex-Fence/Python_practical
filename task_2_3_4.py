# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью,
# у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить
# зарплатную ведомость. Архив с расчётными листками доступен по ссылке
# https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать его вручную
# или самостоятельно научиться делать это с помощью скрипта на Питоне).
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел,
# его зарплата. Сотрудники должны быть упорядочены по алфавиту.

import os
import pathlib
import dload
import xlrd3

#dload.save_unzip('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip','rogaikopyta', delete_after=True)
workdir = os.walk('rogaikopyta')
inventory = {}
for dir_root, tree, file_list in workdir:
    print(dir_root, tree, file_list)
    for file in file_list:
        # print(f'/{dir_root}/{file}')
        with xlrd3.open_workbook(f'{pathlib.Path.cwd()}/{dir_root}/{file}') as wb:
            inventory[wb.sheet_by_index(0).cell_value(1, 1)] = int(wb.sheet_by_index(0).cell_value(1, 3))
            # print(f'{wb.sheet_by_index(0).cell_value(1, 1)} {inventory[wb.sheet_by_index(0).cell_value(1, 1)]}')
num =0
sort_inventory = sorted(inventory.items(), key=lambda x: x[0])

# for i, d in inventory.items():
#     print(f'{i} = {d}')
with open('answer.txt', 'a', encoding = 'utf-8') as answer_file:
    for i in sort_inventory:
        answer_file.write(f'{i[0]} {i[1]}\n')
