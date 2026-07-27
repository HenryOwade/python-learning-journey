from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

all_data = [
    ["Pen", 10, 1.5, 0.05, 14.25],
    ["Book", 5, 4.2, 0.10, 18.90],
    ["Bag", 2, 25, 0.15, 42.50]
]

for row_index, row_data in enumerate(all_data):

    for column in range(1,6):

        sheet.cell(
            row=row_index +1,
            column=column
        ).value = row_data[column - 1]


workbook.save("nested_loop_demo.xlsx")