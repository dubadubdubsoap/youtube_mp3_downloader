#pip install youtube-dl
from __future__ import unicode_literals
import youtube_dl

def check():
    check_done = input('Do you want to enter another song? (Yes/No)')
    if check_done != 'Yes' and check_done != 'No':
        check()
    if check_done == 'Yes':
        return False
    if check_done == 'No':
        return True

def create_songlist():    
    #Create Song List to Download:
    song_list = []
    done = False
    while not done:
        song_input = input('Enter youtube url for song you want to download: ')
        song_list.append(song_input)
        #Check if done:
        done = check()
    return song_list

def download_mp3():
    song_list = create_songlist()
    #Download Songs
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    for song in song_list:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song])
            
            
download_mp3()