import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' 
DOWNLOAD_DIR = 'A:\\Trap'

url = input("playlist url: ")
playlist = Playlist(url)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)