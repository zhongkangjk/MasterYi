import os,sys,django,xlrd
文件名 = '服务费表0417.xls'
读取的Excel = xlrd.open_workbook(filename = 文件名)
文件内第一个表= 读取的Excel.sheet_by_index(0)
# def 获得列序号(表名,查找字段名):
#     列序号 = None
#     for i in range(表名.ncols):
#         if (表名.cell_value(0,i) == 查找字段名):
#             列序号 = i
#             break
#     return 列序号
#横向资料 = [文件内第一个表.row_values(i) for i in range(文件内第一个表.nrows)]
#竖向资料 = [文件内第一个表.col_values(i) for i in range(文件内第一个表.ncols)]
横向资料 = [文件内第一个表.row_values(i) for i in range(1,文件内第一个表.nrows)]
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'shuai.settings'
django.setup()
from search.models import CompanyPost
list = []
for i in 横向资料:
    list.append(CompanyPost(name = i[0],size = i[1],keshou = i[2],note = i[3]))


CompanyPost.objects.bulk_create(list)
