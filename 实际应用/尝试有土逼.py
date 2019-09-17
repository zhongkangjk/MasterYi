from pytube import YouTube
from pprint import pprint
url = 'https://www.youtube.com/watch?v=HK7SPnGSxLM'
yt = YouTube(url)
#yt.streams.filter(only_audio=True).all()   仅列出音频流
#pprint(yt.streams.all())   #全部列表
#pprint(yt.streams.filter(subtype='mp4').all())  #仅MP4
#YouTube(url).streams.first().download()
#video = yt.streams.filter('.mp4')[-1] #检索
#pprint(yt.streams.all())
#yt.streams.all()[-1].download()
audio = yt.streams.filter(only_audio=True).all()
pprint(audio)
audio[0].download()




