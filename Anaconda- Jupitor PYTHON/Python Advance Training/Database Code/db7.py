# Learn to Delete SQL Data
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Create Curser
cursor =conn.cursor()

SQL = """DELETE FROM books WHERE bookid = 1345"""

# Run the SQL Command
cursor.execute(SQL)

print(cursor.rowcount, "row(s) deleted")

# Commit
conn.commit()
# Close the DB Connection
conn.close()

# after running this, Run the DB4.py file to see the records..!!
#%%
