list = [{'1':'a'},{'1':'b'},{'1':'c'},{'1':'来'},{'参数':'a'},{'参数':'二'},{'参数':'c'},{'参数':'d'}]
def get1(name):
    return [i[name] for i in list for j in i if j == name]
print(get1("参数"))



'''
def get(name):
    h1 = []
    for i in list:
        h = [j for j in i if j == name]
        if h != []:
            h1.append(i[h[0]])
    return h1
print(get("参数"))







for i in range(len(list)):
    for j in list[i]:
        name = 'list'+str(j)
        locals()['list' + str(j)] = []
for i in range(len(list)):
    for j in list[i]:
        locals()['list' + str(j)].append(list[i][j])
#print(list1)
#print(list参数)


for i in list:
    print(i)
'''









