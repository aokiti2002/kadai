import sqlite3

def send(company_name, company_employee_data):
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute(
        f"CREATE TABLE {company_name}(id STRING, name STRING, age INTEGER, department STRING)"
    )

    for data in company_employee_data:
        sql = f"INSERT INTO {company_name} (id, name, age, department) values (?,?,?,?)"
        cur.execute(sql, (data["id"], data["name"], data["age"], data["department"]))

    conn.commit()
    conn.close()