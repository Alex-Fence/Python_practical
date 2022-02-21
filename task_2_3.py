# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
# Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты.
# Помогите ему и упорядочите продукты по убыванию калорийности. В случае, если продукты
# имеют одинаковую калорийность - упорядочите их по названию. В качестве ответа необходимо
# сдать названия продуктов, по одному в строке.

import xlrd3
# import wget
# url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
# wget.download(url)

wb = xlrd3.open_workbook('trekking1.xlsx')
sheet = wb.sheet_by_index(0)
dict_groc = {}
for n_row in range(1, 38):
    dict_groc[sheet.cell_value(n_row, 0)] = int(sheet.cell_value(n_row, 1))
# сортировка словаря
for res in sorted(dict_groc.items(), key=lambda x: (-x[1], x[0])):
    print(res[0])
