import openpyxl
import mysql.connector

# connect to database

conn = mysql.connector.connect(
    host = "cp-15.webhostbox.net",
    user = "mongouhd_python",
    password =  "GVvc?zdZQS5V",
    database = "mongouhd_python"
)

# get data from excel

def get_data_from_xl(xlfile,sheetname):
    data = []
    wb = openpyxl.load_workbook(xlfile)
    ws = wb[sheetname]
    for row in ws.values:
        data.append(row)
    return data

# create a table

cursor = conn.cursor(prepared=True)

def create_table():
    SQL = """CREATE TABLE prtmysql(
	years float,
	salary float
	)
"""
    cursor.execute(SQL)
    print("Table Created")


rows = get_data_from_xl("Salary_Data.xlsx","Salary_Data")
create_table()

# insert into table

SQL = """INSERT INTO prtmysql(years, salary)
	values(?,?)"""


cursor.executemany(SQL,rows[1:])

print(cursor.rowcount, "rows inserted")

conn.commit()

#disconnect
conn.close()

