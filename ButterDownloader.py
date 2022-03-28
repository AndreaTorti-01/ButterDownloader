import tkinter
from tkinter import scrolledtext
import sys
from tkinter import filedialog
import variables
import pytube
from threading import Thread
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

BUTTONWIDTH = 16

def folder_selection():
    variables.folder.set(filedialog.askdirectory())

def start_download():
    Thread(target=start_download_t).start()
def start_download_t():
    # download youtube video with pytube to folder
    yt = pytube.YouTube(variables.url.get())
    print("downloading mp4...")
    yt.streams.filter(file_extension='mp4', progressive="True").order_by('resolution').desc().first().download(variables.folder.get())
    print("done!")

def start_download_mp3():
    Thread(target=start_download_mp3_t).start()
def start_download_mp3_t():
    # download youtube video with pytube to folder
    yt = pytube.YouTube(variables.url.get())
    music = yt.streams.filter(file_extension='mp4', progressive="True").order_by('resolution').desc().first()
    print("downloading mp4 before converting to mp3...")
    music.download(output_path=variables.folder.get())
    defaultFilename = music.default_filename
    mp4_file = variables.folder.get() + "\\" + defaultFilename
    mp3_file = variables.folder.get() + "\\" + str(defaultFilename)[0:-3] + "mp3"
    if (os.path.getsize(mp4_file) > 0):
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
    os.remove(mp4_file)
    print("done!")

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.configure(state='normal') # make it writable
        self.textbox.insert(tkinter.END, text) # write text to textbox
        self.textbox.configure(state='disabled') # make it read-only
        self.textbox.see("end") # scroll to the end

    def flush(self): # needed for file like object
        pass

# create printlogger instance
console = scrolledtext.ScrolledText(
    font = "Consolas 9",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    width = 120,
    height = 6
)
pl = PrintLogger(console)
sys.stdout = pl

# create folder input field and button
folderEntry = tkinter.Entry(
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    font = "Arial 14",
    width = 60,
    textvariable = variables.folder
)

folderSelectionButton = tkinter.Button(
    text = "Choose Folder",
    font = "Arial 14",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = BUTTONWIDTH,
    height = 1,
    command = folder_selection
)

# create tkinter label
urlLabel = tkinter.Label(
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    font = "Arial 14",
    text = "Input YouTube URL below:"
)

# create url input field
url = tkinter.Entry(
    font = "Arial 14",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    width = 60,
    textvariable=variables.url
)

# create a button to download the video
downloadButton = tkinter.Button(
    text = "Start Mp4 Download",
    font = "Arial 14",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = BUTTONWIDTH,
    height = 1,
    command = start_download
)

downloadButtonMp3 = tkinter.Button(
    text = "Start Mp3 Download",
    font = "Arial 14",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = BUTTONWIDTH,
    height = 1,
    command = start_download_mp3
)

console.grid(row=0, column=0, columnspan=2)
folderSelectionButton.grid(row=1, column=0, columnspan=2)
folderEntry.grid(row=2, column=0, columnspan=2)
urlLabel.grid(row=3, column=0, columnspan=2)
url.grid(row=4, column=0, columnspan=2)
downloadButton.grid(row=5, column=0)
downloadButtonMp3.grid(row=5, column=1)

# initiate main loop
print("Welcome to ButterDownloader!")
variables.window.mainloop()
