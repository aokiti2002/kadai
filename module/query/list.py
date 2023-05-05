import tkinter
import sqlite3
import re

def send(company_name, box2_list):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    sql_select = f"SELECT * from {company_name}"

    pattern = r"[',()]"

    box2_list.insert(tkinter.END, "id name age department\n")

    for row in cur.execute(sql_select):
        row = str(row)
        row = re.sub(pattern, "", row)
        box2_list.insert(tkinter.END, f"{row}\n")

    conn.commit()
    conn.close()