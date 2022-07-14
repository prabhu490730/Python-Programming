
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Execute any SQL Statement: USE "Curser" to run the queries>> Similar to File Pointer
cursor =conn.cursor()
# Insert into Previous Created for Table in "create_db.py" file.

SQL = """ INSERT INTO books(bookid, title)
values (345, "The 5AM Club")
"""
# Run the SQL Command
cursor.execute(SQL)

# Put Value which is Inserted
print(cursor.rowcount, "row(s) inserted")

# Commit to Overwrite Data in DB
conn.commit()
# Close the DB Connection
conn.close()


#%%
