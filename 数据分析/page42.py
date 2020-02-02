from matplotlib import pyplot
import matplotlib
matplotlib.rc("font",family = 'MicroSoft YaHei',weight="bold")


a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

barh_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+barh_width for i in x_14]
x_16 = [i+barh_width*2 for i in x_14]



#pyplot.bar(range(len(a)),b)
pyplot.barh(x_14,b_14,height=barh_width,label = "14号")
pyplot.barh(x_15,b_15,height=barh_width,label = "15号")
pyplot.barh(x_16,b_16,height=barh_width,label = "16号")


pyplot.legend()


pyplot.yticks(range(len(a)),a)
#pyplot.grid(alpha=0.3)


pyplot.show()