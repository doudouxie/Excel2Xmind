import openpyxl

wb= openpyxl.load_workbook('test.xlsx')
ws = wb.active
for row in range(2,ws.max_row+1):
    if ws[row][4].value is None:
        ws[row][4].value = 'Null'
    if ws[row][5].value is None:
        ws[row][5].value = 'Null'
    if ws[row][3].value is not None:
        case = "/*"+ws[row][6].value+"*/"+ws[row][2].value+"/*"+ws[row][3].value+"*/"
        print(case)
    else:
        case = "/*" + ws[row][6].value + "*/" + ws[row][2].value
        print(case)
    result = ws[row][0].value+"_"+ws[row][1].value+"_"+case+"_"+ws[row][4].value+"_"+ws[row][5].value
    print(result)



