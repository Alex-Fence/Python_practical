import xlrd3

with xlrd3.open_workbook('trekking2.xlsx') as wb:
    sheet0 = wb.sheet_by_index(0)
    sheet1 = wb.sheet_by_index(1)
    product_list = sheet0.col_values(0, 1, 38)
    # список для суммированых показателей всех продуктов
    kall_list_sum = [0, 0, 0, 0]
    for n_row in range(1, 13):
        indx = product_list.index(sheet1.cell_value(n_row, 0))
        kall_list = []
        for energy_val in sheet0.row_values(indx + 1, 1, 5):
            if energy_val == '':
                kall_list.append(0)
            else:
                energy_pack = sheet1.cell_value(n_row, 1)
                kall_list.append(energy_val * energy_pack / 100)
        for i in range(4):
            kall_list_sum[i] += kall_list[i]
    print([int(x) for x in kall_list_sum])
