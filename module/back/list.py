import tkinter
import sqlite3
import re

def system(box1_list, box2_list):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    company_name = box1_list.get()

    sql_select = f"SELECT * from {company_name}"

    pattern = r"[',()]"

    box2_list.insert(tkinter.END, f"{'社員ID':8} {'氏名':5} {'年齢':5} {'所属'}\n")

    for i, row in enumerate(cur.execute(sql_select)):
        row = str(row)
        row = re.sub(pattern, "", row)
        box2_list.insert(tkinter.END, f"{row}\n")
        

    conn.commit()
    conn.close()