from module.front import main
from module.back import delete
import tkinter

#削除画面のUI設定
def show(canvas):
    canvas.place_forget()

    canvas_delete = tkinter.Canvas(width=800, height=450)
    canvas_delete.place(x=0, y=0)

    btn1_delete = tkinter.Button(canvas_delete, text='Top', command=lambda: main.show(canvas_delete))
    btn1_delete.place(x=0, y=0)

    label1_delete = tkinter.Label(text='操作を選択してください')
    label1_delete.place(x=345,y=100)

    btn2_delete = tkinter.Button(canvas_delete, text='会社データ', width=10, command=lambda: show_detail_1(canvas_delete))
    btn2_delete.place(x=350,y=150)

    btn3_delete = tkinter.Button(canvas_delete, text='社員データ', width=10, command=lambda: show_detail_2(canvas_delete))
    btn3_delete.place(x=350,y=200)

#会社データ削除画面のUI設定
def show_detail_1(canvas):
    canvas.place_forget()

    canvas_delete_detail_1 = tkinter.Canvas(width=800, height=600)
    canvas_delete_detail_1.place(x=0, y=0)

    btn1_delete_detail_1 = tkinter.Button(canvas_delete_detail_1, text='Top', command=lambda: main.show(canvas_delete_detail_1))
    btn1_delete_detail_1.place(x=0, y=0)

    label1_delete_detail_1 = tkinter.Label(text='社名を入力してください')
    label1_delete_detail_1.place(x=335,y=100)
    
    box1_delete_detail_1 = tkinter.Entry(canvas_delete_detail_1, width=10)
    box1_delete_detail_1.place(x=350, y=125)

    
    btn2_delete_detail_1 = tkinter.Button(canvas_delete_detail_1, text='削除', width=7, command=lambda: delete.system(box1_delete_detail_1, None))
    btn2_delete_detail_1.place(x=350,y=200)

def show_detail_2(canvas):
    canvas.place_forget()

    canvas_delete_detail_2 = tkinter.Canvas(width=800, height=600)
    canvas_delete_detail_2.place(x=0, y=0)

    btn1_delete_detail_2 = tkinter.Button(canvas_delete_detail_2, text='Top', command=lambda: main.show(canvas_delete_detail_2))
    btn1_delete_detail_2.place(x=0, y=0)

    label1_delete_detail_2 = tkinter.Label(text='社名を入力してください')
    label1_delete_detail_2.place(x=335,y=100)
    
    box1_delete_detail_2 = tkinter.Entry(canvas_delete_detail_2, width=10)
    box1_delete_detail_2.place(x=350, y=125)

    label2_delete_detail_2 = tkinter.Label(text='削除する社員数を入力してください')
    label2_delete_detail_2.place(x=300,y=200)

    box2_delete_detail_2 = tkinter.Entry(canvas_delete_detail_2, width=10)
    box2_delete_detail_2.place(x=350, y=225)

    btn2_delete_detail_2 = tkinter.Button(canvas_delete_detail_2, text='削除', width=7, command=lambda: delete.system(box1_delete_detail_2, box2_delete_detail_2))
    btn2_delete_detail_2.place(x=350,y=300)