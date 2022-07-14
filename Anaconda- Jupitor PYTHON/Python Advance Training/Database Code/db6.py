# Learn to Update Data
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Create Curser
cursor =conn.cursor()

SQL = """UPDATE books SET bookid = bookid + 1000
"""

# Run the SQL Command
cursor.execute(SQL)

print(cursor.rowcount, "row(s) updated")

# Commit
conn.commit()
# Close the DB Connection
conn.close()

# after running this, Run the DB4.py file to see the records..!!
#%%
