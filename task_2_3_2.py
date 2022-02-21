import xlrd3

with xlrd3.open_workbook('trekking2.xlsx') as wb:
    sheet0 = wb.sheet_by_index(0)
    sheet1 = wb.sheet_by_index(1)
    for n_row in range(1, 13):
        sheet1.cell_value(n_row, 0)

