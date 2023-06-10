from pytube import YouTube
from pytube import Playlist

url = input("playlist url: ")
playlist = Playlist(url).video_urls
dir = input("enter path(specify path with double backslashes): ")

for video_link in playlist:
  
    try:
        YouTube(video_link).streams.get_highest_resolution().download(dir)
    
    except:
        print(video_link + " unavailable")

print("Download is completed")