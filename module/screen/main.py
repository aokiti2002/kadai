from module.screen import model, post, put, delete, list
import tkinter

def show(canvas):
    canvas.place_forget()

    canvas_main = tkinter.Canvas(width=800, height=400)
    canvas_main.place(x=0, y=0)

    btn1_main = tkinter.Button(canvas_main, text='新規登録画面', width=10, command=lambda: post.show(canvas_main))
    btn1_main.place(x=350,y=125)

    btn2_main = tkinter.Button(canvas_main, text='更新画面', width=10, command=lambda: put.show(canvas_main))
    btn2_main.place(x=350,y=150)

    btn3_main = tkinter.Button(canvas_main, text='削除画面', width=10, command=lambda: delete.show(canvas_main))
    btn3_main.place(x=350,y=175)

    btn4_main = tkinter.Button(canvas_main, text='一覧画面', width=10, command=lambda: list.show(canvas_main))
    btn4_main.place(x=350,y=200)

    model.screen.mainloop()