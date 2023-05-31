from module.front import main
from module.back import post
import tkinter

#新規登録画面のUI設定
def show(canvas):
    canvas.place_forget()

    canvas_post = tkinter.Canvas(width=800, height=450)
    canvas_post.place(x=0, y=0)

    btn1_post = tkinter.Button(canvas_post, text='Top', command=lambda: main.show(canvas_post))
    btn1_post.place(x=0, y=0)

    label1_post = tkinter.Label(text='社名を入力してください')
    label1_post.place(x=335,y=100)
    
    box1_post = tkinter.Entry(canvas_post, width=10)
    box1_post.place(x=350, y=125)

    label2_post = tkinter.Label(text='社員数を入力してください')
    label2_post.place(x=325,y=200)

    box2_post = tkinter.Entry(canvas_post, width=10)
    box2_post.place(x=350, y=225)

    btn2_post = tkinter.Button(canvas_post, text='登録', width=7, command=lambda: post.system(box1_post, box2_post))
    btn2_post.place(x=350,y=300)