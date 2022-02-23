# Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня,
# названия продукта и его количества в граммах. Для каждого дня посчитайте 4 числа:
# суммарную калорийность и граммы белков, жиров и углеводов.
# Числа округлите до целых вниз и введите через пробел.
# Информация о каждом дне должна выводиться в отдельной строке.

import xlrd3

def resoult_by_day(list_sum):
    res_by_day = [int(x) for x in list_sum]
    print(f'{res_by_day[0]} {res_by_day[1]} {res_by_day[2]} {res_by_day[3]}')

# def calculate(wb, sheet0, sheet1)
#     indx = product_list.index(sheet1.cell_value(n_row, 1))
#     kall_list = []
#     for energy_val in sheet0.row_values(indx + 1, 1, 5):
#         if energy_val == '':
#             kall_list.append(0)
#         else:
#             energy_pack = sheet1.cell_value(n_row, 2)
#             kall_list.append(energy_val * energy_pack / 100)
#     for i in range(4):
#         kall_list_sum[i] += kall_list[i]
#     return kall_list_sum

with xlrd3.open_workbook('trekking3.xlsx') as wb:
    sheet0 = wb.sheet_by_index(0)
    sheet1 = wb.sheet_by_index(1)
    product_list = sheet0.col_values(0, 1, 38)
    # список для суммированых показателей всех продуктов
    kall_list_sum = [0, 0, 0, 0]
    n_day = sheet1.cell_value(1, 0)
    for n_row in range(1, 100):
        if n_day == sheet1.cell_value(n_row, 0):

            indx = product_list.index(sheet1.cell_value(n_row, 1))
            kall_list = []
            for energy_val in sheet0.row_values(indx + 1, 1, 5):
                if energy_val == '':
                    kall_list.append(0)
                else:
                    energy_pack = sheet1.cell_value(n_row, 2)
                    kall_list.append(energy_val * energy_pack / 100)
            for i in range(4):
                kall_list_sum[i] += kall_list[i]
        else:
            resoult_by_day(kall_list_sum)
            kall_list_s = [0, 0, 0, 0]
            indx = product_list.index(sheet1.cell_value(n_row, 1))
            kall_list = []
            for energy_val in sheet0.row_values(indx + 1, 1, 5):
                if energy_val == '':
                    kall_list.append(0)
                else:
                    energy_pack = sheet1.cell_value(n_row, 2)
                    kall_list.append(energy_val * energy_pack / 100)
            for i in range(4):
                kall_list_sum[i] += kall_list[i]
            n_day = sheet1.cell_value(n_row, 0)

    resoult_by_day(kall_list_sum)
    # print(sheet1.cell_value(n_row, 1))

