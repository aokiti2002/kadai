import tkinter

#UI生成
def make():
    global screen, canvas
    
    screen = tkinter.Tk()
    screen.geometry('800x450')

    canvas = tkinter.Canvas(width=800, height=450)
    canvas.place(x=0, y=0)