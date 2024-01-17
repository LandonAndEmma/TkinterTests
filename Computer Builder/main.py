from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import time
root = Tk()
root.title('Computer Builder')
root.geometry('300x480')
home = PhotoImage(file='home.png')
root.iconphoto(False,home)
var = StringVar()
purplecomputer = PhotoImage(file="purple.png")
bluecomputer = PhotoImage(file="blue.png")
orangecomputer = PhotoImage(file="orange.png")
greencomputer = PhotoImage(file="green.png")
def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("RAM Downloader")
    newWindow.geometry("300x177")
    wifi = PhotoImage(file='wifi.png')
    newWindow.iconphoto(True,wifi)
    def update_progress_label():
        return f"Current Progress: {pb['value']}%"
    def progress():
        while pb['value'] < 100:
            time.sleep(0.05)
            pb['value'] += 1
            value_label['text'] = update_progress_label()
        else:
            showinfo(title='Download Complete!',message='You have downloaded free RAM!')
    def stop():
        pb.stop()
        value_label['text'] = update_progress_label()
    def close():
        newWindow.destroy()
    pb = Progressbar(newWindow,orient='horizontal',mode='determinate',length=280)
    pb.pack()
    value_label = Label(newWindow, text=update_progress_label())
    value_label.pack()
    rambuttonimage2 = PhotoImage(file='ram.png')
    start_button = Button(newWindow, command=progress, image=rambuttonimage2)
    start_button.pack()
    stopbuttonimage = PhotoImage(file='stop.png')
    stop_button = Button(newWindow, command=stop, image=stopbuttonimage)
    stop_button.pack()
    close_button = Button(newWindow, command=close, image=closebuttonimage)
    close_button.pack()
    pb.mainloop()
    value_label.mainloop()
    start_button.mainloop()
    stop_button.mainloop()
    close_button.mainloop()
def closeroot():
    root.destroy()
def purple():
    canvas.create_image(125,150, image=purplecomputer, anchor=CENTER, state=NORMAL)
    canvas.pack()
def blue():
    canvas.create_image(125,150, image=bluecomputer, anchor=CENTER, state=NORMAL)
    canvas.pack()
def orange():
    canvas.create_image(125,150, image=orangecomputer, anchor=CENTER, state=NORMAL)
    canvas.pack()
def green():
    canvas.create_image(125,150, image=greencomputer, anchor=CENTER, state=NORMAL)
    canvas.pack()
rb1 = Radiobutton(root, text='Purple', variable=var, value=purple, command=purple)
rb1.pack()
rb2 = Radiobutton(root, text='Blue', variable=var, value=blue, command=blue)
rb2.pack()
rb3 = Radiobutton(root, text='Orange', variable=var, value=orange, command=orange)
rb3.pack()
rb4 = Radiobutton(root, text='Green', variable=var, value=green, command=green)
rb4.pack()
rambuttonimage1 = PhotoImage(file='download_ram.png')
rambutton = Button(root, command=openNewWindow, image=rambuttonimage1)
rambutton.pack()
canvas = Canvas(root, width = 250, height = 300)
canvas.pack()
canvas.create_image(125, 150, image=purplecomputer, anchor=CENTER, state=NORMAL)
closebuttonimage = PhotoImage(file='close.png')
closeroot_button = Button(root, command=closeroot, image=closebuttonimage,)
closeroot_button.pack()
root.mainloop()
rb1.mainloop()
rb2.mainloop()
rb3.mainloop()
rb4.mainloop()
canvas.mainloop()
rambutton.mainloop()