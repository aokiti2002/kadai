import tkinter

def make():
    global screen, canvas
    
    screen = tkinter.Tk()
    screen.geometry('800x400')

    canvas = tkinter.Canvas(width=800, height=400)
    canvas.place(x=0, y=0)