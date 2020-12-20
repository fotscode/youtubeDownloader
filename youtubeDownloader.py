from tkinter import filedialog
from tkinter import *
import os
import pytube

#Main Screen
master = Tk()
master.title("YouTube Downloader")
master.iconbitmap(r'images/youtube.ico')
master.configure(bg="#FFBC42")

#Default folder
folder = os.getcwd()


#Functions


def downloadVideo(video):
    try: 
        title = video.title
        video = video.streams.filter(only_audio=True).first()# gets the video file
        out_file=video.download(folder)
        new_file=title+".mp3"
        os.rename(out_file,new_file)# renames file, .mp4 to .mp3
        notifDownload.config(fg="green",text="Download Completed")# writes in green if succeeded
    except Exception as e:
        print(e)
        notifDownload.config(fg="red",text="Video couldn't be downloaded") # writes in red if failed

def downloadVideoButton():
    video_url = url.get()
    try:
        video = pytube.YouTube(video_url)
        downloadVideo(video)
    except Exception as e:
        print(e)
        notifDownload.config(fg="red",text="Video couldn't be downloaded")

def downloadPlaylistButton():
    playlist_url = url.get()
    try:
        playlist = pytube.contrib.playlist.Playlist(playlist_url) # gets playlist object
        listOfVideos = playlist.videos # makes a list of all the video's objects contained in the playlist
        os.chdir(folder)
        listFileNames=os.listdir('.') # makes a list of all the files in the current directory
        listFileNamesStripped=[]

        for fileName in listFileNames:
            listFileNamesStripped.append(fileName.strip(".mp3")) # removes ".mp3" from string

        # here checks if there are repeated songs
        for video in listOfVideos:
            title = video.title
            if title not in listFileNamesStripped:
                downloadVideo(video)
            else:
                notifDownload.config(fg="red",text="Song Repeated: "+title)

    except Exception as e:
        print(e)
        notifDownload.config(fg="red",text="Link isn't valid")

def searchPath():
    global folder
    folder = filedialog.askdirectory()
    notifPath.config(text=folder)# writes in green the folder directory 

#GUI

Label(master, text="YouTube Downloader",bg="#FFBC42",fg="red",font=("Calibri",22,"bold")).grid(sticky=N,padx=100,row=0)

#Playlist link
Label(master,text="Please enter the link to your playlist/video below:", bg="#FFBC42",font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
url = StringVar()
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
#Buttons

Button(master,width=15,bg="black",fg="white",text="Download Playlist",font=("Calibri",12),command=downloadPlaylistButton).grid(sticky=SW,row=3,padx=80,pady=15,ipadx=10)
Button(master,width=15,bg="black",fg="white",text="Download Video",font=("Calibri",12),command=downloadVideoButton).grid(sticky=SE,row=3,padx=80,pady=15,ipadx=10)


#Notification Download
notifDownload = Label(master,bg="#FFBC42",font=("Calibri",12,"bold"))
notifDownload.grid(sticky=N,pady=1,row=4)

#Choose path
Label(master,text="Directory:",bg="#FFBC42",font=("Calibri",14,"bold")).grid(sticky=N,row=5,pady=14)
Button(master,width=20,bg="black",fg="white",text="Choose path",font=("Calibri",12),command=searchPath).grid(sticky=N,row=6,pady=15)

#Notification Path
notifPath= Label(master,text=folder,bg="#FFBC42",fg="black",font=("Calibri",8))
notifPath.grid(sticky=N,row=7,pady=15)

master.mainloop()




