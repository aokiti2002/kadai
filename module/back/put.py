from module.function import generate
import tkinter
import sqlite3
import random
import names

#PUTメソッド設定
def system(box1_put, box2_put):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    company_name = box1_put.get()
    company_employees_number = int(box2_put.get())

    box1_put.delete(0, tkinter.END)
    box2_put.delete(0, tkinter.END)

    company_employees_data = generate.employee_info(company_name, company_employees_number)

    for data in company_employees_data:
        sql_insert = f"INSERT INTO {company_name} (id, name, age, department) values (?,?,?,?)"
        cur.execute(sql_insert, (data["id"], data["name"], data["age"], data["department"]))

    conn.commit()
    conn.close()