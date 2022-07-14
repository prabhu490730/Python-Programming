
import sqlite3
conn = sqlite3.connect("mydatabase.db")
# Create Curser
cursor =conn.cursor()

mybooks = [(455, "Discovery of INDIA"),
        (489, "India after Gandhi"),
        (970, "Wings of Fire")]

SQL = """ INSERT INTO books(bookid, title)
values(?,?)
"""

# Run the SQL Command
cursor.executemany(SQL,mybooks) # executemany for multiple execute table
print(cursor.rowcount, "row(s) inserted")

# Commit
conn.commit()
# Close the DB Connection
conn.close()

# after running this, Run the DB4.py file..!!


#%%
