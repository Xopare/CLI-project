import tkinter
import time
from turtle import back, position

def GUItime():

    return time.strftime('%I:%M %p')


def GUI():
    window = tkinter.Tk()
    window.geometry("1280x720")
    window.attributes('-fullscreen',True)

    bg = tkinter.PhotoImage(file = "./Resources/GUI/BG.png")
    background_label = tkinter.Label(window, image= bg)
    background_label.place(x = 0 , y = 0 , relwidth= 1 , relheight= 1 )

    timeGUI = tkinter.Label(window,text = GUItime(),font = ("Arial",10), bg ="White")
    timeGUI.place(x = 0 , y = 0)

    quitGlobal = tkinter.Button(window, text="x", command = quit ,font = ("Arial",10))
    quitGlobal.place(x = 1255 , y = 1, width= 20 , height= 20)
    window.mainloop()


if __name__ == '__main__':
    GUI()