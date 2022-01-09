import os
#os.system('cd ' + os.getcwd()) --don't run, this is just to grab the current filepath for debugging
os.system('pyinstaller.exe -F --add-data "ffmpeg.exe;." --add-data "ffplay.exe;." --add-data "ffprobe.exe;." youtube_downloader.py')