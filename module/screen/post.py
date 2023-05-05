from module.screen import main
from module.query import post
import tkinter
import random
import json
import names
import os

def show(canvas):
    canvas.place_forget()

    canvas_post = tkinter.Canvas(width=800, height=400)
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

    btn2_post = tkinter.Button(canvas_post, text='登録', width=7, command=lambda: back())
    btn2_post.place(x=350,y=300)

    def back():
        company_name = box1_post.get()
        employee_numbers = int(box2_post.get())
        company_departments = ["Accounting", "Finance", "Planning", "Sales", "Engineering", "Design", "Management"]
        company_employees_data = []

        for i in range(0, employee_numbers):
            id = company_name + "_" + str(random.randint(1000, 9999))
            name = names.get_full_name()
            age = random.randint(20, 50)
            department = random.choice(company_departments)

            company_employees_data.append({"id":id, "name":name, "age":age, "department":department})

        with open(f"{company_name}_employees_data.json", "w") as f:
            json.dump(company_employees_data, f, indent=2)
    
        with open(f"{company_name}_employees_data.json", "r") as f:
            company_employees_data = json.load(f)

        json_files = [f for f in os.listdir('.') if f.endswith('.json')]

        for file in json_files: 
            os.remove(file)

        box1_post.delete(0, tkinter.END)
        box2_post.delete(0, tkinter.END)

        post.send(company_name, company_employees_data)

    