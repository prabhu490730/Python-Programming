import openpyxl
import mysql.connector

# connect to database

conn = mysql.connector.connect(
    host = "cp-15.webhostbox.net",
    user = "mongouhd_python",
    password =  "GVvc?zdZQS5V",
    database = "mongouhd_python"
)

# function to write data to xl

def write_to_xl(xlfile,data):
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save(xlfile)


cursor = conn.cursor(prepared=True)

cursor.execute("SELECT * FROM iprabhatkumar")

rows = cursor.fetchall()

rows.insert(0,cursor.column_names) # insert the header row

write_to_xl("exported_data.xlsx",rows)


#disconnect
conn.close()

#%%
