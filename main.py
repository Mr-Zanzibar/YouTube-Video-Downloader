class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   
from pytube import YouTube
from colorama import init
init(autoreset=True)


link = input("Enter a YouTube link: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print(f" ")
print(color.GREEN + f' Download Completed!')
print(f" ")
