a = '1231565679887'
res = []
for i in range(0,len(a)):
	a1 = a[i+1:]
	for j in range(0,len(a1)):
		if a1[j] == a[i]:
			res.append(a[i+1:j+i+1])
reslen = res[0]
for i in res[1:]:
	if len(i) > len(reslen):
		reslen = i
print(reslen)