from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube import Playlist
import os
import sys
import colorama
from colorama import Fore, Style

from pytube import YouTube
url = input(Fore.LIGHTBLACK_EX + "enter Youtube link here: " + Style.BRIGHT)
print("Enter the destination for mp4 file(leave blank for current directory)")
destination1 = str(input(">> ")) or '.'
print("Enter the destination for mp3 file(leave blank for current directory)")
destination2 = str(input(">> ")) or '.'
video = YouTube(url)
colorama.init()
name = video.title
print(Fore.RED + "Title: ",name)
print(Fore.RED + "Author: ",video.author)
print(Fore.RED + "Length: ",video.length)
print(Fore.RED + "Views: ",video.views)
print(Fore.RED + "Publication date: ",video.publish_date)
old_name = YouTube(url).streams.get_highest_resolution().download(output_path=destination1)
base, ext = os.path.splitext(old_name)
new_name = base + "--video.mp4"
os.rename(old_name, new_name)
print(Fore.YELLOW + "Download 1 completed" + Style.DIM)
from pytube import YouTube
import os
yt = YouTube(
    str(url))
video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path=destination2)
base, ext = os.path.splitext(out_file)
new_file = base + '--audio.mp3'
os.rename(out_file, new_file)
print(Fore.YELLOW + "Download 2 completed" + Style.DIM)
exit()