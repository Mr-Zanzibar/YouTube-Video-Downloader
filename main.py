from pytube import YouTube

link = input("Enter a YouTube link: ")
yt = YouTube(link)

yt = yt.streams.get_highest_resolution()
ys.download()
print("Download Completed!")
