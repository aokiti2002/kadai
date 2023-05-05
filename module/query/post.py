import sqlite3

def send(company_name, company_employees_data):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    sql_create = f"CREATE TABLE {company_name}(id STRING, name STRING, age INTEGER, department STRING)"
    cur.execute(sql_create)

    for data in company_employees_data:
        sql_insert = f"INSERT INTO {company_name} (id, name, age, department) values (?,?,?,?)"
        cur.execute(sql_insert, (data["id"], data["name"], data["age"], data["department"]))

    conn.commit()
    conn.close()