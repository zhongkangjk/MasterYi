from matplotlib import pyplot


x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

#设置图片大小
pyplot.figure(figsize = (20,8),dpi=80)


#绘图
pyplot.plot(x,y)

pyplot.xticks(range(2,25)) #设置x的刻度



#保存
pyplot.savefig("./t1.png")

#展示图形
pyplot.show()