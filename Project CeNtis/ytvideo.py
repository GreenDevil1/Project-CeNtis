from pytube import YouTube
from colorama import Fore, Style
import colorama

url = input(Fore.LIGHTBLACK_EX + "enter Youtube link here: " + Style.BRIGHT)
dir = input("path: ")
video = YouTube(url)
colorama.init()
print(Fore.RED + "Title: ",video.title)
print(Fore.RED + "Author: ",video.author)
print(Fore.RED + "Length: ",video.length)
print(Fore.RED + "Views: ",video.views)
print(Fore.RED + "Publication date: ",video.publish_date)
YouTube(url).streams.get_highest_resolution().download(dir)
print(Fore.YELLOW + "Download completed" + Style.DIM)
exit()