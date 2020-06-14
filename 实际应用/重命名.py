import os, sys
os.chdir(sys.path[0])
files=os.listdir()

# for i in files:
#     新名称 = i.split('-')[-1].strip()
#     os.rename(i,新名称)

# listmusic = []
# for i in files:
#     if i[-3:] == 'mp3':
#         listmusic.append(i)
# for i in range(0,len(listmusic)):
#     新名称 = str(i+1)+ '-' +listmusic[i]
#     os.rename(listmusic[i],新名称)
for i in files:
    print(i)