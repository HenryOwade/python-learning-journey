from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

row_data = ["Pen", 10, 1.5, 0.05, 14.25]

for column in range(1, 6):
    sheet.cell(row=1, column=column).value = row_data[column - 1]

workbook.save("row_demo.xlsx")
