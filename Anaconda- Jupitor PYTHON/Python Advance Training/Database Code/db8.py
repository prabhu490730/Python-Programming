# Create Table and then Select Table in the Same Code
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Create Curser
cursor =conn.cursor()

mybooks = [(7, "JAMES BOND"),
           (490, "Prabhu Rockstar"),
           (730, "The Shining Blaze")]

SQL = """ INSERT INTO books(bookid, title)
values(?,?)
"""

# Run the SQL Command
cursor.executemany(SQL,mybooks) # executemany for multiple execute table
print(cursor.rowcount, "row(s) inserted")

# Commit
conn.commit()

# here you can use Select to fetch table in same code
SQL = """ SELECT * FROM books"""

# Run the SQL Command
cursor.execute(SQL)
result = cursor.fetchall()

for row in result:
    print(row)

# Close the DB Connection
conn.close()

#%%
