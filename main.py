class color:
   GREEN = '\033[92m'


import colorama   
from pytube import YouTube


link = input('Enter a YouTube link: ')
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print(f' ')
print(color.GREEN + f' Download Completed!')
print(f' ')
