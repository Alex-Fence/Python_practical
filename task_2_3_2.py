import xlrd3

with xlrd3.open_workbook('trekking2.xlsx') as wb:
    sheet0 = wb.sheet_by_index(0)
    sheet1 = wb.sheet_by_index(1)
    product_list = sheet0.col_values(0, 1, 38)
    # for prod in product_list:
    #     print(f'{prod} {product_list.index(prod)}')
    kall_list = []
    for n_row in range(1, 13):
        indx = product_list.index(sheet1.cell_value(n_row, 0))
        # print(f'{indx} {product_list[indx]} {sheet1.cell_value(n_row, 0)}  {sheet0.row_values(indx+1, 0, 5)}')
        # kall_list = []
        # kall_list.append(product_list[indx])
        for energy_val in sheet0.row_values(indx+1, 1, 5):
            if energy_val == '':
                kall_list.append(0)
            else:
                energy_pack = sheet1.cell_value(n_row, 1)
                kall_list.append(energy_val*energy_pack/100)
        print(f'{int(kall_list[1])} {int(kall_list[2])} {int(kall_list[3])} {int(kall_list[4])}')

