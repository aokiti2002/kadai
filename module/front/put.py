from module.front import main
from module.back import put
import tkinter

#更新画面のUI設定
def show(canvas):
    canvas.place_forget()

    canvas_put = tkinter.Canvas(width=800, height=450)
    canvas_put.place(x=0, y=0)

    btn1_put = tkinter.Button(canvas_put, text='Top', command=lambda: main.show(canvas_put))
    btn1_put.place(x=0, y=0)

    label1_put = tkinter.Label(text='社名を入力してください')
    label1_put.place(x=335,y=100)
    
    box1_put = tkinter.Entry(canvas_put, width=10)
    box1_put.place(x=350, y=125)

    label2_put = tkinter.Label(text='追加する社員数を入力してください')
    label2_put.place(x=300,y=200)

    box2_put = tkinter.Entry(canvas_put, width=10)
    box2_put.place(x=350, y=225)

    btn2_put = tkinter.Button(canvas_put, text='更新', width=7, command=lambda: put.system(box1_put, box2_put))
    btn2_put.place(x=350,y=300)