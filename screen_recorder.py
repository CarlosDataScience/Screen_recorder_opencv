import cv2
from tkinter import *
import numpy as np
import pyautogui

resolution=(1920,1080)
continueRecording=True

codec= cv2.VideoWriter_fourcc(*'XVID')
filename="screen.avi"
fps=60
out=cv2.VideoWriter(filename, codec,fps,resolution)


def recordOneFrame():
    global continueRecording
    img = pyautogui.screenshot()
    frame = np.array(img)

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)

    if continueRecording:
        window.after(round(1/60.*1000), recordOneFrame)


window=Tk()
window.title("Screen Recorder")
window.geometry("400x150")
window.config(bg="lightblue")


def record_Screen(event):
    window.iconify()
    recordOneFrame()



recordButton= Button(window, text="Record",font=("Bell MT",20),width=20, command=record_Screen)
recordButton.pack(pady=(10,0))

def stop_recording(event):
    global continueRecording
    continueRecording=False
    window.destroy()
    out.release()



stopButton = Button(window,text=("Stop"), font=("Bell MT",20), width=20, command= stop_recording)
stopButton.pack(pady=(10,0))



mainloop()


cv2.destroyAllWindows()
out.release()
