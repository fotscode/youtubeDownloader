from tkinter import filedialog
from tkinter import *
import os
import pytube

#Main Screen
master = Tk()
master.title("Youtube Downloader")


#Default folder
folder = "C:/Users/cacut/Desktop/projects/youtubeDownloader/videos"


#Functions

def downloadPlaylist():
    playlist_url = url.get()
    playlist = pytube.contrib.playlist.Playlist(playlist_url) # gets playlist object
    listOfUrls = playlist.video_urls # makes a list of all the video's urls contained in the playlist
    for videoUrl in listOfUrls:
        try:
            yt = pytube.YouTube(videoUrl)
            title = yt.title
            video = yt.streams.filter(only_audio=True).first()
            out_file=video.download(folder)
            
            new_file=title+".mp3"
            os.chdir(folder)
            os.rename(out_file,new_file) # renames file, .mp4 to .mp3
            notifDownload.config(fg="green",text="Download Completed") # writes in green if succeeded
        except Exception as e:
            print(e)
            notifDownload.config(fg="red",text="Video couldn't be downloaded") # writes in red if failed

def searchPath():
    global folder
    folder = filedialog.askdirectory()
    notifPath.config(fg="green",text=folder) # writes in green the folder directory 

#GUI

Label(master, text="Youtube Converter",fg="red",font=("Calibri",15,"bold")).grid(sticky=N,padx=100,row=0)

#Playlist link
Label(master,text="Please enter the link to your playlist below:", font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
url = StringVar()
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
#Button
Button(master,width=20,text="Download",font=("Calibri",12),command=downloadPlaylist).grid(sticky=N,row=3,pady=15)

#Notification Download
notifDownload = Label(master,font=("Calibri",12))
notifDownload.grid(sticky=N,pady=1,row=4)

#Choose path
Label(master,text="Directory",font=("Calibri",14)).grid(sticky=N,row=5,pady=15)
Button(master,width=20,text="Choose path",font=("Calibri",12),command=searchPath).grid(sticky=N,row=6,pady=15)

#Notification Path
notifPath= Label(master,font=("Calibri",8))
notifPath.grid(sticky=N,row=7,pady=15)

master.mainloop()




