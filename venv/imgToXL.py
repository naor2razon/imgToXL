import xlsxwriter
#CREATE WORKBOOL & WORKSHEET
workbook = xlsxwriter.Workbook('img.xlsx')
worksheet = workbook.add_worksheet()
#SET COLUMN
worksheet.set_column('A:A',30)
#INSERT IMG
worksheet.write('A2','Insert an image:')
worksheet.insert_image('imageName.png')

workbook.close()