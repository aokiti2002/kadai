from module.function import generate
import tkinter
import sqlite3
import os
import json

def system(box1_post, box2_post):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    company_name = box1_post.get()
    company_employees_number = int(box2_post.get())

    box1_post.delete(0, tkinter.END)
    box2_post.delete(0, tkinter.END)

    company_employees_data = generate.employee_info(company_name, company_employees_number)

    with open(f"{company_name}_employees_data.json", "w") as f:
        json.dump(company_employees_data, f, indent=2)
    
    with open(f"{company_name}_employees_data.json", "r") as f:
        company_employees_data = json.load(f)

    json_files = [f for f in os.listdir('.') if f.endswith('.json')]

    for file in json_files: 
        os.remove(file)

    sql_create = f"CREATE TABLE {company_name}(id STRING, name STRING, age INTEGER, department STRING)"
    cur.execute(sql_create)

    for data in company_employees_data:
        sql_insert = f"INSERT INTO {company_name} (id, name, age, department) values (?,?,?,?)"
        cur.execute(sql_insert, (data['id'], data['name'], data['age'], data['department']))

    conn.commit()
    conn.close()