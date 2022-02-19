# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал
# зарплаты для разных интересные ему профессий. Таблица доступна по ссылке
# https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. Выведите название региона с самой
# высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после его упорядочивания) и,
# через пробел, название профессии с самой высокой средней зарплатой по всем регионам.

import xlrd3
# import wget
from statistics import median_high, mean

# url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
# wget.download(url)
wb = xlrd3.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)
# вычисление медианы ЗП по регионам
median_list_reg = {}
for n_row in range(1, 9):
    row_of_sheet = sheet.row_values(rowx=n_row, start_colx=1, end_colx=8)
    info_cell = sheet.cell_value(n_row, 0)
    median_list_reg[info_cell] = median_high([int(cell_vol) for cell_vol in row_of_sheet])
    print(f"{info_cell} {median_high([int(cell_vol) for cell_vol in row_of_sheet])}")
# вычисление средней ЗП
mean_list_pro = {}
for n_col in range(1, 8):
    col_of_sheet = sheet.col_values(n_col, 1, 9)
    info_cell = sheet.cell_value(0, n_col)
    mean_list_pro[info_cell] = mean([int(cell_vol) for cell_vol in col_of_sheet])
    print(f"{info_cell} {mean([int(cell_vol) for cell_vol in col_of_sheet])}")
print(max(median_list_reg, key=median_list_reg.get), ' ', max(mean_list_pro, key=mean_list_pro.get))
