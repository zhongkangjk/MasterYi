import re
mystr = """<s>1597<s>"""
restr = "<s>\d+<s>"
restr1 = "<s>(\d+)<s>"
regex = re.compile(restr,re.IGNORECASE)
regex1 = re.compile(restr1,re.IGNORECASE)
mylist = regex.findall(mystr)
mylist1 = regex1.findall(mystr)
print(mylist)
print(mylist1)