from openpyxl import load_workbook

workbook = load_workbook("practice_file_1.xlsx")

print(workbook)
print(type(workbook))
print(workbook.sheetnames)
print(type(workbook.sheetnames))

sheet = workbook["Sales"]

print(sheet)
print(type(sheet))

print(sheet["A1"])
print(type(sheet["A1"]))

print(sheet["A1"].value)

print(sheet.cell(row=1, column=1))
print(sheet.cell(row=1, column=1).value)