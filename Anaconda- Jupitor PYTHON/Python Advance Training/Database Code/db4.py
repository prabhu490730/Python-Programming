
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Execute any SQL Statement: USE "Curser" to run the queries>> Similar to File Pointer
cursor =conn.cursor()

SQL = """ SELECT * FROM books"""

# Run the SQL Command
cursor.execute(SQL)
result = cursor.fetchall()

for row in result:
    print(row)

# Close the DB Connection
conn.close()

#%%
