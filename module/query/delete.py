import sqlite3

def send(company_name, employee_name):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    if employee_name is None:
        sql_drop = f"DROP TABLE IF EXISTS {company_name}"
        cur.execute(sql_drop)
    else:
        sql_delete = f"DELETE FROM {company_name} WHERE name = '{employee_name}'"
        cur.execute(sql_delete)
    
    conn.commit()
    conn.close()