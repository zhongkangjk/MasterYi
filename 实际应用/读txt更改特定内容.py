import re
with open('test.txt','r+',encoding='UTF-8') as f:
	a = f.read()
	b = re.sub('\[目标就是你][\s\S]*\[','[xinde]'+'\n'+'neirongt'+'\n\n'+'[',a)
	f.seek(0)
	f.truncate()
	f.write(b)