import xlrd
import os

def ArrangeInDirectory(path,directory,extn):
    if(os.path.isfile(path)):
        pass

wb = xlrd.open_workbook("C:\Test_Excel_Read\DemoSheet.xlsx")
sheet = wb.sheet_by_index(0)
#row = sheet.cell(0,0)

for i in range(1,sheet.nrows):
    #print(i)
    row_slc = sheet.row_slice(i,0,3)
    print(row_slc[0].value)
    print(row_slc[1].value)
    print(row_slc[2].value)
    print( row_slc[2].value.split(','))