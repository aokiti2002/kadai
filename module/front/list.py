from module.front import main
from module.back import list
import tkinter

#一覧画面のUI設定
def show(canvas):
    canvas.place_forget()

    canvas_list = tkinter.Canvas(width=800, height=450)
    canvas_list.place(x=0, y=0)

    btn1_list = tkinter.Button(canvas_list, text='Top', command=lambda: main.show(canvas_list))
    btn1_list.place(x=0, y=0)

    box1_list = tkinter.Entry(canvas_list, width=10)
    box1_list.place(x=325, y=100)

    box2_list = tkinter.Text(canvas_list, width=60, height=20)
    box2_list.place(x=185, y=150)

    btn2_list = tkinter.Button(canvas_list, text='検索', command=lambda: list.system(box1_list, box2_list))
    btn2_list.place(x=425,y=100)