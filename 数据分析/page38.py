from matplotlib import pyplot
import matplotlib
matplotlib.rc("font",family = 'MicroSoft YaHei',weight="bold")

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

pyplot.figure(figsize=(20,8),dpi=80)

x = range(1,32)
pyplot.scatter(x,y_3,label = "3月份")
pyplot.scatter(x,y_10,label = "10月份")
pyplot.legend()


pyplot.xlabel("时间")
pyplot.ylabel("温度")
pyplot.title("标题")
pyplot.show()