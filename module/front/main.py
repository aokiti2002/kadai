from module.front import model, post, put, delete, list
import tkinter

#メイン画面のUI設定
def show(canvas):
    canvas.place_forget()

    canvas_main = tkinter.Canvas(width=800, height=450)
    canvas_main.place(x=0, y=0)

    label_main = tkinter.Label(canvas_main, text='ペーパーカンパニー作成ツール', fg="red", font=("", 50, "bold", "italic"))
    label_main.place(x=75, y=100)

    btn1_main = tkinter.Button(canvas_main, text='新規登録画面', width=10, command=lambda: post.show(canvas_main))
    btn1_main.place(x=350,y=200)

    btn2_main = tkinter.Button(canvas_main, text='更新画面', width=10, command=lambda: put.show(canvas_main))
    btn2_main.place(x=350,y=225)

    btn3_main = tkinter.Button(canvas_main, text='削除画面', width=10, command=lambda: delete.show(canvas_main))
    btn3_main.place(x=350,y=250)

    btn4_main = tkinter.Button(canvas_main, text='一覧画面', width=10, command=lambda: list.show(canvas_main))
    btn4_main.place(x=350,y=275)

    model.screen.mainloop()