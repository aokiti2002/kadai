import tkinter
import sqlite3

#DELETEメソッド設定
def system(box1_delete, box2_delete):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    if box2_delete is None:
        company_name = box1_delete.get()

        box1_delete.delete(0, tkinter.END)

        sql_drop = f"DROP TABLE IF EXISTS {company_name}"
        cur.execute(sql_drop)
    else:
        company_name = box1_delete.get()
        company_employees_number = box2_delete.get()

        box1_delete.delete(0, tkinter.END)
        box2_delete.delete(0, tkinter.END)

        sql_delete = f"DELETE FROM {company_name} WHERE name = '{employee_name}'"
        cur.execute(sql_delete)
    
    conn.commit()
    conn.close()