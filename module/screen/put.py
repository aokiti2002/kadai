from module.screen import main
from module.query import put
import tkinter
import random
import names

def show(canvas):
    canvas.place_forget()

    canvas_put = tkinter.Canvas(width=800, height=400)
    canvas_put.place(x=0, y=0)

    btn1_put = tkinter.Button(canvas_put, text='Top', command=lambda: main.show(canvas_put))
    btn1_put.place(x=0, y=0)

    label1_put = tkinter.Label(text='社名を入力してください')
    label1_put.place(x=335,y=100)
    
    box1_put = tkinter.Entry(canvas_put, width=10)
    box1_put.place(x=350, y=125)

    label2_put = tkinter.Label(text='追加する社員数を入力してください')
    label2_put.place(x=325,y=200)

    box2_put = tkinter.Entry(canvas_put, width=10)
    box2_put.place(x=350, y=225)

    btn2_put = tkinter.Button(canvas_put, text='更新', width=7, command=lambda: back())
    btn2_put.place(x=350,y=300)

    def back():
        company_name = box1_put.get()
        employee_numbers = int(box2_put.get())
        company_departments = ["Accounting", "Finance", "Planning", "Sales", "Engineering", "Design", "Management"]
        company_employees_data = []

        for i in range(0, employee_numbers):
            id = company_name + "_" + str(random.randint(1000, 9999))
            name = names.get_full_name()
            age = random.randint(20, 50)
            department = random.choice(company_departments)

            company_employees_data.append({"id":id, "name":name, "age":age, "department":department})

        box1_put.delete(0, tkinter.END)
        box2_put.delete(0, tkinter.END)

        put.send(company_name, company_employees_data)


