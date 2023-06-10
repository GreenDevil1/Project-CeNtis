from pytube import YouTube
from pytube import Playlist

url = input("playlist url: ")
playlist = Playlist(url).video_urls
print(playlist)