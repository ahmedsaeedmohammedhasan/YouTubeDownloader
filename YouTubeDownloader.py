from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk
import threading

root = Tk()
root.title("YouTube Downloader")
root.geometry("600x320")
root.resizable(False, False)

#MY Functions

def browse():
    directory = filedialog.askdirectory(title="Save Video")
    folderLink.delete(0, "end")
    folderLink.insert(0, directory)

def down_yt():
    status.config(text="Status: Downloading...")
    link = ytlink.get()
    folder = folderLink.get()
    YouTube(link, on_progress_callback=progress, on_complete_callback=finish).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").asc().first().download(folder)


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Wait, your video is Downloading now")

def finish(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status: Complete")

#Youtube Logo
ytLogo = PhotoImage(file="official-youtube-icon-28.png").subsample(15)
ytTitle = Label(root, image=ytLogo)
ytTitle.place(relx=0.5, rely=0.25, anchor="center")


#YOUTUBE link URL

ytlabel = Label(root, text="Youtube Link")
ytlabel.place(x=25, y=150)

ytlink = Entry(root, width=60)
ytlink.place(x=140, y=150)

#Download Folder

folderLabel =  Label(root, text="Download Folder")
folderLabel.place(x=25, y=183)

folderLink = Entry(root, width=50)
folderLink.place(x=140, y=183)

#Browse Button

browse = ttk.Button(root, text="Browse", command=browse)
browse.place(x=455, y=180)

#Dpwnload Button

download = ttk.Button(root, text="Download", command=threading.Thread(target=down_yt).start)
download.place(x=250, y=220)

#status bar

status = Label(root, text="Status: Ready", font="Calibre 10 italic", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)

root.mainloop()