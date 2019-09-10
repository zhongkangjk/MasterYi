from lxml import etree
import xlrd
root = etree.Element("Data",TYPE="KEHUBIANMA")
FENLEI = etree.SubElement(root, "FENLEI")
#Row = etree.SubElement(FENLEI,"Row")
wenjianjia = {"PID":"0","O_BM":"100","O_PID":"0","BM":"100","MC":"第一文件夹"}
FENLEI.append(etree.Element("Row",wenjianjia))
KHXX = etree.SubElement(root, "KHXX")
dk = xlrd.open_workbook(filename = "待转换.xlsx")#打开文件
sheet1 = dk.sheet_by_index(0)
def 获得列序号(表名,查找字段名):
    列序号 = None
    for i in range(表名.ncols):
        if (表名.cell_value(0,i) == 查找字段名):
            列序号 = i
            break
    return 列序号
序号列 = sheet1.col_values(获得列序号(sheet1,"序号"),1)
文件夹列 = sheet1.col_values(获得列序号(sheet1,"文件夹"),1)
企业名称列 = sheet1.col_values(获得列序号(sheet1,"企业名称"),1)
税号列 = sheet1.col_values(获得列序号(sheet1,"税号"),1)
地址列 = sheet1.col_values(获得列序号(sheet1,"地址"),1)
银行列 = sheet1.col_values(获得列序号(sheet1,"银行"),1)
行数 = sheet1.nrows -1
for x in range(0,行数):
    i = int(x)
    编码 = ['',文件夹列[i],'','',税号列[i],银行列[i],序号列[i],文件夹列[i],序号列[i],地址列[i],企业名称列[i]]
    keys = ["KZ1","PID","YJDZ","JM","NSRSBH","YHZH","O_BM","O_PID","BM","DZ","MC"]
    客户信息 = dict(zip(keys,编码))
    KHXX.append(etree.Element("Row",客户信息))
#root.append(etree.Element("child1"))   添加子
tree = etree.ElementTree(root)
tree.write("结果.xml", pretty_print=True, xml_declaration=True, encoding='GB18030')