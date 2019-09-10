import xlrd
import xlwt

整个表格 = xlrd.open_workbook(filename="表格.xlsx")
第一个表 = 整个表格.sheet_by_index(0)
第二个表 = 整个表格.sheet_by_index(1)  # 按顺序
可收列表 = 第二个表.col_values(1, 1)
可收列表2 = 第一个表.col_values(1, 1)
第三个表 = 整个表格.sheet_by_index(2)
全部列表 = 第三个表.col_values(0, 1)
时间列表 = 第三个表.col_values(1, 1)
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
# worksheet.write(1,1050, label = 'this is test')
for line in 可收列表2:
    if line in 全部列表:
        x = 可收列表2.index(line)
        n = 全部列表.index(line)
        时间 = 时间列表[n]
        try:
            worksheet.write(x,0,label=时间)
        except Exception:
            pass
        continue


workbook.save('2.xls')


