# ██▓    ▄▄▄     ▓██   ██▓▄▄▄█████▓ ▒█████   ███▄    █  ▄▄▄          ▄▄▄▄    ██▓    ▄▄▄     ▓██   ██▓
#▓██▒   ▒████▄    ▒██  ██▒▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █ ▒████▄       ▓█████▄ ▓██▒   ▒████▄    ▒██  ██▒
#▒██░   ▒██  ▀█▄   ▒██ ██░▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄     ▒██▒ ▄██▒██░   ▒██  ▀█▄   ▒██ ██░
#▒██░   ░██▄▄▄▄██  ░ ▐██▓░░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██    ▒██░█▀  ▒██░   ░██▄▄▄▄██  ░ ▐██▓░
#░██████▒▓█   ▓██▒ ░ ██▒▓░  ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒   ░▓█  ▀█▓░██████▒▓█   ▓██▒ ░ ██▒▓░
#░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░   ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ 
#░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░     ░      ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░   ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░ 
#  ░ ░    ░   ▒   ▒ ▒ ░░    ░      ░ ░ ░ ▒     ░   ░ ░   ░   ▒       ░    ░   ░ ░    ░   ▒   ▒ ▒ ░░  
#    ░  ░     ░  ░░ ░                  ░ ░           ░       ░  ░    ░          ░  ░     ░  ░░ ░     
#                 ░ ░                                                     ░                  ░ ░     


from select import select
from tkinter import *
from tkinter import filedialog, PhotoImage
from turtle import title
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube import Playlist
from distutils.core import setup
import os

import shutil


#Functions
def on_close():
    screen.destroy()

def get_current_directory():
    path = os.getcwd()
    return path

current_directory = get_current_directory()
current_directory = current_directory#+"/Project CeNtis"

def select_path():
    #allows user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_mp4_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #download video
    mp4_audio = YouTube(get_link).streams.get_highest_resolution().download()
    audio = VideoFileClip(mp4_audio)
    audio.close()
    #move file to selected directory
    shutil.move(mp4_audio, user_path)
    screen.title("Download Complete! Download another file...")

def download_mp3_file():
    destination2 = path_label.cget("text")
    screen.title("Downloading...")
    yt = YouTube(
    str(link_field.get()))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination2)
    base, ext = os.path.splitext(out_file)
    new_file = base + '--audio.mp3'
    os.rename(out_file, new_file)
    screen.title("Download Complete! Download another file...")

def download_file():
    #download mp4(video_file)
    destination1 = path_label.cget("text")
    screen.title("Downloading...")
    old_name = YouTube(link_field.get()).streams.get_highest_resolution().download(output_path=destination1)
    base, ext = os.path.splitext(old_name)
    new_name = base + "--video.mp4"
    os.rename(old_name, new_name)
    screen.title("Download 1 completed")
    screen.title("Starting download 2")

    #download mp3(audio_file)
    destination2 = path_label.cget("text")
    screen.title("Downloading...")
    yt = YouTube(
    str(link_field.get()))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination2)
    base, ext = os.path.splitext(out_file)
    new_file = base + '--audio.mp3'
    os.rename(out_file, new_file)
    screen.title("Download Complete! Download another file...")  

def download_playlist_mp4_and_mp3_():
    destination3 = path_label.cget("text")
    screen.title("Downloading...")
    p = Playlist(link_field.get())
    for video in p.videos:
        #video.streams.first().download(output_path=destination3)
        video.streams.get_highest_resolution().download(output_path=destination3)
    screen.title("Download Complete! Download another file...")
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
global screen
screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()
screen.protocol("WM_DELETE_WINDOW", on_close)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Setze die Hintergrundfarbe des Canvas auf dunkelgrau
canvas.configure(bg="#333333")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#image logo
logo_img = PhotoImage(file = current_directory+"\yt.png")
#resize
logo_img = logo_img.subsample(12, 12)
canvas.create_image(250, 80, image=logo_img)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", fg="white", bg="#333333")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#select path for saving file
path_label = Label(screen, text="select path for download", fg="white", bg="#333333")
select_btn = Button(screen, text="Select", command=None)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#download btn for both mp4 and mp3
download_btn = Button(screen, text="mp4 and mp3", command=download_file)
#add mp4 btn to canvas
canvas.create_window(250, 390, window=download_btn)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#download btn for mp4
download_mp4_btn = Button(screen, text="mp4", command=download_mp4_file)
#add mp4 btn to canvas
canvas.create_window(180, 390, window=download_mp4_btn)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#download btn for mp3
download_mp3_btn = Button(screen, text="mp3", command=download_mp3_file)
#add mp3 btn to canvas
canvas.create_window(320, 390, window=download_mp3_btn)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#download btn for playlist
download_playlist_btn = Button(screen, text="playlist", command=download_playlist_mp4_and_mp3_)
#add playlist btn to canvas
canvas.create_window(250, 450, window=download_playlist_btn)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
screen.mainloop()

# name: 76 97 121 116 111 110 97  66 108 97 121 
# version: 1.0.0
# country: Germany