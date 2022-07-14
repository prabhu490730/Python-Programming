# export table to csv

import csv
import sqlite3

f=open("books.csv","w")
writer = csv.writer(f)

# create a database connection
conn = sqlite3.connect("mydatabase.db")

# create cursor
cursor =conn.cursor()

SQL = """ SELECT * FROM books"""

# run the SQL command
cursor.execute(SQL)

result = cursor.fetchall()

for row in result:
    writer.writerow(row)

f.close()
# close the database connection
conn.close()
#%%
