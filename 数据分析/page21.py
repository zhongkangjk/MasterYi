from matplotlib import pyplot
import random
import matplotlib
from matplotlib import font_manager




#字体
# font = {
#     'family':'MicroSoft YaHei',
#     'weight':'bold',
#     #'size':'large'
#     }
# matplotlib.rc("font",**font)
matplotlib.rc("font",family = 'MicroSoft YaHei',weight="bold")

#另一种字体
#my_font = font_manager.FontProperties(fname="路径.ttc")
#加参数fontproperties=my_font


x = range(0,120)
y = [random.randint(20,35) for i in range(120)]


pyplot.figure(figsize = (20,8),dpi = 80)

pyplot.plot(x,y)


#调整x轴的刻度
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]

#取步长，数字和字符串一一对应，数据的长度一样
pyplot.xticks(list(x)[::3],_xtick_labels[::3],rotation=270)  #rotation旋转角度

#添加描述信息
pyplot.xlabel("时间")
pyplot.ylabel("温度")
pyplot.title("10Ian到12点每分钟的气温变化情况")



pyplot.show()
