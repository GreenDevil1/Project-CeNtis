# -----------------------------------------------------------importing code----------------------------------------------------------------------

from typing import final
import colorama
from colorama import Fore
from colorama import Style
from sys import stdout
from time import sleep
from colorama.initialise import reset_all
from cryptography.fernet import Fernet
import os
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip
import phonenumbers
import folium
from phonenumbers import geocoder
import runpy
import shutil
import subprocess
from datetime import datetime
# ----------------------------------------------------------------code-------------------------------------------------------------------------------- 

# -------------------------------------------------------main logo + projekt name-------------------------------------------------------------
def jump_to_function(func):
    func()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_directory():
    path = os.getcwd()
    path = path.replace('/', '\\')
    return path

current_directory = get_current_directory()
current_directory_origin = current_directory
current_directory = current_directory+"\\Project CeNtis"

def main():
    colorama.init()
    print(Fore.MAGENTA + "")
    f= open(current_directory+"\\test12.txt", "r")
    content = f.read()
    msg = "Project CeNtis"
    print(content)
    colorama.init()
    f.close()

# --------------------------------------------introduction containing program information-----------------------------------------------------
    print(Fore.BLACK + "" + Style.RESET_ALL)
    print(Fore.BLACK+"__________________________________________"+Fore.RED+"The CeNtis-Allrounder Toolkit"+Style.BRIGHT+Fore.LIGHTMAGENTA_EX+ "(CAT)"+Style.BRIGHT+Style.RESET_ALL)
    print(Fore.BLACK+"_____________________________________________"+Fore.RED+"Created by: "+Style.BRIGHT+Fore.LIGHTRED_EX+"GreenDevil1"+Style.BRIGHT+Fore.LIGHTMAGENTA_EX+"(Gr33T)"+Style.BRIGHT+Style.RESET_ALL)
    print(Fore.BLACK+"___________________________________________________"+Fore.RED+"Version: "+Style.BRIGHT+Fore.LIGHTRED_EX+"1.0.0 "+Style.BRIGHT+Style.RESET_ALL)
    print(Fore.BLACK+"__________________________________________________"+Fore.YELLOW+"Codename: " +Style.BRIGHT+Fore.LIGHTWHITE_EX+ "Ligma"+Style.BRIGHT+Style.RESET_ALL)
    print(Fore.BLACK+"____________________________________"+Fore.YELLOW+"Welcome to the CeNtis-Allrounder Toolkit"+Style.BRIGHT+Fore.LIGHTMAGENTA_EX+ "(CAT)"+Style.BRIGHT+Style.RESET_ALL+Fore.YELLOW+"."+Style.RESET_ALL)
    print(Fore.BLACK+"_______________________________________"+Fore.YELLOW+"The most silent and underated allrounder."+Style.BRIGHT+Style.RESET_ALL)
    print("")
    print("")
    print(Fore.BLACK+"____________________________"+Style.BRIGHT+Fore.BLACK+"The CeNtis-Allrounder Toolkit is a product of Urmomholdings."+Style.RESET_ALL)
    print("")
    print("")
    print(Fore.BLACK+"___________________________________________"+Style.BRIGHT+Fore.BLACK+"Visit: https://www.urmomgay.com "+Style.RESET_ALL)
    print("")
    print("")
    print(Fore.BLACK+"________________________________________"+Style.BRIGHT+Fore.BLACK+"It´s easy to update using ur Moms pc!"+Style.RESET_ALL)
    print(Fore.BLACK+"_________________"+Style.BRIGHT+Fore.BLACK+"Visit https://github.com/GreenDevil1/Project-CeNtis to update all your tools!"+Style.RESET_ALL)
    print("")
    print("")
    
# --------------------------------------------------------main selection menu-----------------------------------------------------------------
    
    print("Select from the menu: ")
    print("")
    print("  1) Encryption Tool")
    print("  2) YT Downloader")
    print("  3) Phonenumber tracker")
    print("  4) Delete Folder")
    print("  5) Delete Logs since installation")
    print("")
    print(" 99) Exit the CeNtis-Allrounder Toolkit")

# ----------------------------------------------------------Encryption tool----------------------------------------------------------------
    frage = input()
    clear_terminal()
    if frage == "1":
            colorama.init()
            text1 = (Fore.RED + " !!! penguin is now activated !!!" + Style.RESET_ALL)           
            for char in text1:
                stdout.write(char)
                stdout.flush()
                sleep(0.1)
            print(Fore.LIGHTBLUE_EX + "")
            f= open(current_directory+"\\Penguin.txt", "r")
            content = f.read()
            msg = "penguin"
            print(content)
            colorama.init()
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "welcome to "+ msg + Style.RESET_ALL)
            f.close()
            
            def main(): 
                print("Select tool from the menu: ")
                print("")
                print("  1) Encryption")
                print("  2) Decription")
                print("")
                print(" 99) Exit")
            
                frage = input()
    
# ----------------------------------------------------------Encryption tool----------------------------------------------------------------
                clear_terminal()
                if frage == "1":
                        colorama.init()
                        text2 = (Fore.MAGENTA + "!!! Encryption tool activated !!!" + Style.RESET_ALL)
                        print(text2)
                        print("")
                        from cryptography.fernet import Fernet
                        import os
                        txt = input("textdokument(e.g. example.txt): ")
                        with open(txt) as f:
                            mytxt = ''.join(f.readlines())
                        keyname = input("name for key: ")
                        key = Fernet.generate_key()
                        f = open(keyname + ".txt", "wb")
                        f.write(key)
                        f.close()
            
                        encryptedtxt = input("name for encrypted textdokument: ")
                        keyname = Fernet(key)
                        mytxtbyt = bytes(mytxt, 'utf-8') 
                        encrypted = keyname.encrypt(mytxtbyt)
                        f = open(encryptedtxt + ".txt", "wb")
                        f.write(encrypted)
                        f.close()
                        if os.path.exists(txt):
                            os.remove(txt)
                        else:
                            print(Fore.RED + Style.BRIGHT + "File is not available" + Style.RESET_ALL)
    
# ----------------------------------------------------------Decryption tool-----------------------------------------------------------------
                elif frage == "2":
                        colorama.init()
                        text3 = (Fore.MAGENTA + "!!! Decryption tool activated !!!" + Style.RESET_ALL)
                        print(text3)
                        print("")

                        from cryptography.fernet import Fernet
                        encryptedfile = input("encryptedfile(e.g. encryptedfile.txt): ")
                        ogfile = input("name of original file: ")
                        with open(encryptedfile) as f:
                            encogfile = ''.join(f.readlines())
                            encogfilebyt = bytes(encogfile, 'utf-8')
                        f.close()
                        
                        key = input("key(e.g. key.txt):")
                        with open(key) as f:
                            key = ''.join(f.readlines())
                            keybyt = bytes(key, 'utf-8')
                        f.close()
                        
                        keytouse = Fernet(keybyt)
                        myPass = (keytouse.decrypt(encogfilebyt))
                        print(myPass)
                        import sys
                        import os
                        original_stdout = sys.stdout
                        with open(ogfile + ".txt", "w") as f:
                            sys.stdout = f
                            print(myPass)
                            sys.stdout = original_stdout
    
# ----------------------------------------------------------Exit first tool-----------------------------------------------------------------
                elif frage == "99":
                    exit()
                else:
                    print(Fore.RED + "!!! Error please try again !!!" + Style.BRIGHT)
                    restart = input("Do you wish to restart again? \
                    [Y/N]")
                    if restart == "Y":
                        main()
                    else :
                        exit()
            main()

# ----------------------------------------------------------Youtube downloader---------------------------------------------------------------
    elif frage == "2":
            colorama.init()
            text4 = (Fore.RED + " !!! Penguins land is now activated !!!" + Style.RESET_ALL)
            for char in text4:
                stdout.write(char)
                stdout.flush()
                sleep(0.1)
            colorama.init()
            f= open(current_directory+"\\Penguins land.txt", "r")
            content = f.read()
            msg = "penguins land"
            print(content)
            print(Fore.LIGHTGREEN_EX + "welcome to ",msg + Style.DIM)
            f.close()

            def main():
                print("Select from menu: ")
                print("")
                print("  1) Download YouTube video (mp4)")
                print("  2) Download YouTube playlist (mp4-format)")
                print("  3) Convert mp4 to mp3")
                print("  4) Download mp4 and mp3")
                print("  5) Open GUI")
                print("")
                print(" 98) Return")
                print(" 99) Exit")
# ---------------------------------------------------------Download YouTube video------------------------------------------------------------   
                frage = input()
                clear_terminal()
                if frage == "1":
                        text5 = (Fore.MAGENTA + "!!! download yt video tool activated !!!"+ Style.DIM)
                        print(text5)
                        print("")
                        from pytube import YouTube
                        url = input(Fore.LIGHTBLACK_EX + "enter Youtube link here: " + Style.BRIGHT)
                        video = YouTube(url)
                        colorama.init()
                        print(Fore.RED + "Title: ",video.title)
                        print(Fore.RED + "Author: ",video.author)
                        print(Fore.RED + "Length: ",video.length)
                        print(Fore.RED + "Views: ",video.views)
                        print(Fore.RED + "Publication date: ",video.publish_date)
                        YouTube(url).streams.get_highest_resolution().download()
                        print(Fore.YELLOW + "Download completed" + Style.DIM)
                        exit()
# ---------------------------------------------------------Download YouTube playlist---------------------------------------------------------
                elif frage == "2":
                        text8= (Fore.MAGENTA + "!!! download yt playlist tool activated !!!"+ Style.DIM)
                        print(text8)
                        print("")
                        url = input("playlist url: ")
                        playlist = Playlist(url).video_urls
                        dir = input("enter path(specify path with double backslashes): ")
                        
                        for video_link in playlist:
                            
                            try:
                                YouTube(video_link).streams.get_highest_resolution().download(dir)
                            
                            except:
                                print(video_link + " unavailable")
                        
                        print(Fore.YELLOW + "Download is completed" + Style.RESET_ALL)
                        exit()

# ---------------------------------------------------------Convert mp4 to mp3----------------------------------------------------------------
                elif frage == "3":
                        text6 = (Fore.MAGENTA + "!!! conversion tool activated !!!" + Style.DIM)
                        print(text6)
                        input("")
                        from moviepy.editor import VideoFileClip
        
                        mp4_file = input(Fore.RED + "mp4 filename: " + Style.RESET_ALL)
                        mp3_file = mp4_file + ".mp3" 
        
                        videoclip = VideoFileClip(mp4_file + ".mp4")
        
                        audioclip = videoclip.audio
                        audioclip.write_audiofile(mp3_file)
        
                        audioclip.close()
                        videoclip.close()
                        exit()
# ---------------------------------------------------------Download mp4 and mp3----------------------------------------------------------------              
                elif frage == "4":
                        text5 = (Fore.MAGENTA + "!!! download yt video tool activated !!!"+ Style.DIM)
                        print(text5)
                        print("")
                        print("options: ")
                        print("  1) same directory")
                        print("  2) two different directories")
                        frageOPTIONSdirectories = input()
                        if frageOPTIONSdirectories == "1":
                                from pytube import YouTube
                                url = input(Fore.LIGHTBLACK_EX + "enter Youtube link here: " + Style.BRIGHT)
                                print("Enter the destination (leave blank for current directory)")
                                destination1 = str(input(">> ")) or '.'
                                destination2 = destination1
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
                                destination = str() or '.'
                                out_file = video.download(output_path=destination2)
                                base, ext = os.path.splitext(out_file)
                                new_file = base + '--audio.mp3'
                                os.rename(out_file, new_file)
                                print(Fore.YELLOW + "Download 2 completed" + Style.DIM)
                                exit()
                        if frageOPTIONSdirectories == "2":
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
                elif frage == "5":
                    runpy.run_path(current_directory+"\\downloadtest.pyw")
                    jump_to_function(main)   

# ----------------------------------------------------------Exit YT Download tool---------------------------------------------------------------
                elif frage == "99":
                    exit()
                else:
                    print(Fore.RED + "!!! Error please try again !!!" + Style.BRIGHT)
                    
                    restart = input("Do you wish to restart again? \
                    [Y/N]")
                    if restart == "Y":
                        main()
                    else :
                        exit()
            main()           

# ----------------------------------------------------------Phonenumber tracker------------------------------------------------------------------
    elif frage == "3":
            text7 = (Fore.MAGENTA + "!!! Phonenumber Tracker activated !!!" + Style.BRIGHT)
            for char in text7:
                stdout.write(char)
                stdout.flush()
                sleep(0.1)
            print("")
            colorama.init()
            f= open("TiCKoveN.txt", "r")
            content = f.read()
            msg = "TiCKoveN"
            print(content)
            print(Fore.LIGHTGREEN_EX + "welcome to ",msg + Style.DIM)
            f.close()
            def main():
                print(" 1) START tool")
                print(" 2) EXIT tool")
# ----------------------------------------------------------Start Phonetracker-------------------------------------------------------------------
                frage3 = input()
                clear_terminal()
                if frage3 == "1":
                        import phonenumbers
                        import folium
                        from phonenumbers import geocoder
                        number = input("Phonenumber: ")
                        Key = ""
                        samNumber = phonenumbers.parse(number)
                        yourLocation = geocoder.description_for_number(samNumber, "en")
                        print(yourLocation)
                        from phonenumbers import carrier
                        service_provider = phonenumbers.parse(number)
                        print(carrier.name_for_number(service_provider, "en"))
                        from opencage.geocoder import OpenCageGeocode
                        geocoder = OpenCageGeocode(Key)
                        query = str(yourLocation)
                        results = geocoder.geocode(query)
                        lat = results[0]["geometry"]["lat"]
                        lng = results[0]["geometry"]["lng"]
                        print(lat,lng)
                        myMap = folium.Map(location=[lat, lng], zoom_start_=9)
                        folium.Marker([lat, lng],popup= yourLocation).add_to((myMap))
                        myLocationdatei = input("Location file name: ")
                        finalll = myLocationdatei + ".html"
                        myMap.save(finalll)

# ----------------------------------------------------------Exit Phonetracker----------------------------------------------------------------                
                elif frage3 == "2":
                    colorama.init()
                    print(Fore.RED + "Bye" + Style.RESET_ALL)
                    exit()
                
                else:
                    print(Fore.RED + "!!! Error please try again !!!" + Style.BRIGHT)
                    restart = input("Do you wish to restart again? \
                    [Y/N]")
                    if restart == "Y":
                        main()
                    else :
                        exit()
            main()

# ----------------------------------------------------------Exit main menu------------------------------------------------------------------------
    elif frage == "99":
        colorama.init()
        print(Fore.RED + "Bye" + Style.RESET_ALL)
        exit()

# ----------------------------------------------------------Help,credits and about----------------------------------------------------------------
    elif frage == "4":
        def delete_folder(path):
            shutil.rmtree(path)
        
        delete_folder(current_directory_origin)
    
    elif frage == "5":
        def delete_logs(since):
            since_date = datetime.strptime(since, "%Y-%m-%d")
            cmd = f"""
            $logs = Get-WinEvent -ListLog *;
            foreach ($log in $logs) {{
                $logName = $log.LogName;
                try {{
                    $logEntries = Get-WinEvent -FilterHashtable @{{ LogName=$logName; StartTime='{since_date}' }} -ErrorAction Stop;
                    foreach ($entry in $logEntries) {{
                    Remove-WinEvent -LogName $logName -FilterXPath "*[System[(EventRecordID=$($entry.Id))]]";
                    }}
                }} catch {{}}
            }}
            """
            subprocess.run(["powershell", "-Command", cmd], check=True)

        with open("date_of_installation.txt", "r") as f:
            since = f.read().strip()

        delete_logs(since)

# ----------------------------------------------------------False number in main menu-------------------------------------------------------------
    else:
        print(Fore.RED + " !!! Error unknown number please try again !!!" + Style.RESET_ALL)
        restart = input("Do you wish to restart again? \
        [Y/N]")
        if restart == "Y":
            print(" Still in progress ")
        else :
            exit()
main()