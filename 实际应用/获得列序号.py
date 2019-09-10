import xlrd
dk = xlrd.open_workbook(filename = "工作簿1.xlsx")
sheet1 = dk.sheet_by_index(0)
def 获得列序号(表名,查找字段名):
    列序号 = None
    for i in range(表名.ncols):
        if (表名.cell_value(0,i) == 查找字段名):
            列序号 = i
            break
    return 列序号
名称列 = sheet1.col_values(获得列序号(sheet1,"名称"),2)
服务期限 = sheet1.col_values(获得列序号(sheet1,"服务期限"),2)
整行 = []