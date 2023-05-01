from module.screen import main
import tkinter

def show(canvas):
    canvas.place_forget()

    canvas_put = tkinter.Canvas(width=800, height=400)
    canvas_put.place(x=0, y=0)

    btn1_put = tkinter.Button(canvas_put, text='Top', command=lambda: main.show(canvas_put))
    btn1_put.place(x=0, y=0)

    label1_put = tkinter.Label(text='操作を選択してください')
    label1_put.place(x=325,y=100)

    btn2_put = tkinter.Button(canvas_put, text='社員データ更新', width=10, command=lambda: show_detail_1(canvas_put))
    btn2_put.place(x=350,y=150)

    btn3_put = tkinter.Button(canvas_put, text='社員データ追加', width=10, command=lambda: show_detail_2(canvas_put))
    btn3_put.place(x=350,y=200)

def show_detail_1(canvas):
    canvas.place_forget()

    canvas_put_detail_1 = tkinter.Canvas(width=800, height=400)
    canvas_put_detail_1.place(x=0, y=0)

    btn1_put_detail_1 = tkinter.Button(canvas_put_detail_1, text='Top', command=lambda: main.show(canvas_put_detail_1))
    btn1_put_detail_1.place(x=0, y=0)

    label1_put_detail_1 = tkinter.Label(text='社名を入力してください')
    label1_put_detail_1.place(x=335,y=100)
    
    box1_put_detail_1 = tkinter.Entry(canvas_put_detail_1, width=10)
    box1_put_detail_1.place(x=350, y=125)

    label2_put_detail_1 = tkinter.Label(text='更新する社員名を入力してください')
    label2_put_detail_1.place(x=325,y=200)

    box2_put_detail_1 = tkinter.Entry(canvas_put_detail_1, width=10)
    box2_put_detail_1.place(x=350, y=225)

def show_detail_2(canvas):
    canvas.place_forget()

    canvas_put_detail_2 = tkinter.Canvas(width=800, height=400)
    canvas_put_detail_2.place(x=0, y=0)

    btn1_put_detail_2 = tkinter.Button(canvas_put_detail_2, text='Top', command=lambda: main.show(canvas_put_detail_2))
    btn1_put_detail_2.place(x=0, y=0)

    label1_put_detail_2 = tkinter.Label(text='社名を入力してください')
    label1_put_detail_2.place(x=335,y=100)
    
    box1_put_detail_2 = tkinter.Entry(canvas_put_detail_2, width=10)
    box1_put_detail_2.place(x=350, y=125)

    label2_put_detail_2 = tkinter.Label(text='追加する社員数を入力してください')
    label2_put_detail_2.place(x=325,y=200)

    box2_put_detail_2 = tkinter.Entry(canvas_put_detail_2, width=10)
    box2_put_detail_2.place(x=350, y=225)

