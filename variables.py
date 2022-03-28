import tkinter

palette = {
  "bg": "#4a4d4d",
  "fg": "#ffffff",
  "activebackground": "#656868",
  "activeforeground": "#ffffff"
}

window = tkinter.Tk()
window.geometry("960x540")
window.configure(bg= palette["bg"])
window.title('ButterDownloader')

for c in range (2):
    window.columnconfigure(c, weight=1)
for r in range (6):
    window.rowconfigure(r, weight=1)

folder = tkinter.StringVar(window)
url = tkinter.StringVar(window)

window.update()